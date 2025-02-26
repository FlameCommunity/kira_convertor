import os
import subprocess
import datetime
from PIL import Image
import imageio
import numpy as np

# !!! DON'T TOUCH IF YOU DON'T KNOW WHAT YOU ARE DOING !!! #
def print_colored(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    print(f"{colors[color]}{text}{colors['reset']}")

def get_timestamp():
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def log_message(log_file, message):
    timestamp = get_timestamp()
    log_file.write("-----------------------------------------------------------------------------")
    log_file.write(f"\n{timestamp} :\n{message}\n")
    log_file.write("-----------------------------------------------------------------------------\n")

def convert_to_tga(input_path, output_path):
    img = Image.open(input_path)
    img_array = np.array(img)
    imageio.imwrite(output_path, img_array, format='tga')

def convert_to_dds(input_path, output_path):
    texconv_path = os.path.join(os.path.dirname(__file__), "texconv.exe")

    if not os.path.exists(texconv_path):
        raise FileNotFoundError(f"[X] texconv.exe was not found in {texconv_path}. Make sure it is in the script's folder.")

    command = [
        texconv_path,
        '-o', os.path.dirname(output_path),
        '-ft', 'dds',
        '-f', 'BC3_UNORM',
        '-srgb',
        '-m', '1',
        input_path
    ]
    subprocess.run(command, check=True)

def get_format_choice(message):
    format_options = {
        "1": "png",
        "2": "jpg",
        "3": "dds",
        "4": "tga",
        "5": "webp"  # NEW WEBP
    }
    while True:
        print("\nSelect the format:")
        for key, value in format_options.items():
            print(f"{key} = {value}")
        choice = input(f"{message} ")
        if choice in format_options:
            return format_options[choice]
        print_colored("[X] Invalid option! Please choose a valid number.", "red")

def convert_image(input_path, output_path, output_format, log_file):
    try:
        print_colored(f"Processing: {input_path} -> {output_path}", "blue")

        if output_format == 'dds':
            convert_to_dds(input_path, output_path)
        elif output_format == 'tga':
            convert_to_tga(input_path, output_path)
        else:
            img = Image.open(input_path)
            if output_format == "webp":
                img.save(output_path, format="WEBP", quality=90)  # Save WebP with quality 90
            else:
                img.save(output_path, format=output_format.upper())

        log_message(log_file, f"[OK] Successfully converted: {input_path} -> {output_path}")
        print_colored(f"[OK] Successfully converted: {output_path}", "green")
    except Exception as e:
        log_message(log_file, f"[X] Error during conversion: {input_path} -> {output_path} | {e}")
        print_colored(f"[X] Error during conversion: {input_path} -> {output_path} | {e}", "red")

def main():
    input_folder = "input"
    output_folder = "output"
    log_path = "log.txt"

    if not os.path.exists(input_folder):
        print_colored(f"[X] The folder '{input_folder}' does not exist! Create it and add images.", "red")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    input_format = get_format_choice("Enter the initial format: ")
    output_format = get_format_choice("Which format do you want to convert to: ")

    with open(log_path, "a", encoding="utf-8") as log_file:
        files_found = False

        for file_name in os.listdir(input_folder):
            if file_name.lower().endswith(f".{input_format}"):
                files_found = True
                input_path = os.path.join(input_folder, file_name)
                output_file = os.path.splitext(file_name)[0] + f".{output_format}"
                output_path = os.path.join(output_folder, output_file)
                convert_image(input_path, output_path, output_format, log_file)

        if not files_found:
            log_message(log_file, f"[X] No files found with the extension .{input_format} in '{input_folder}'.")
            print_colored(f"[X] No files found with the extension .{input_format} in '{input_folder}'.", "red")

if __name__ == "__main__":
    main()
