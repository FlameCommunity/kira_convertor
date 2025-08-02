import os
import subprocess
import datetime
import time
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
	log_file.write("-----------------------------------------------------------------------------\n")
	log_file.write(f"{timestamp} :\n{message}\n")
	log_file.write("-----------------------------------------------------------------------------\n")

def record_sys_error(syserr_path, message):
	# Open in append mode and write the error line
	with open(syserr_path, "a", encoding="utf-8") as err_file:
		err_file.write(f"{get_timestamp()} : {message}\n")

def convert_to_tga(input_path, output_path):
	img = Image.open(input_path)
	img_array = np.array(img)
	imageio.imwrite(output_path, img_array, format='tga')

def convert_to_dds(input_path, output_path):
	texconv_path = os.path.join(os.path.dirname(__file__), "texconv.exe")
	if not os.path.exists(texconv_path):
		raise FileNotFoundError(f"texconv.exe not found in {texconv_path}")
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
		"5": "webp",
		"6": "ico",
		"7": "bmp"
	}
	while True:
		print("\nSelect the format:")
		for key, value in format_options.items():
			print(f"{key} = {value}")
		choice = input(f"{message} ")
		if choice in format_options:
			return format_options[choice]
		print_colored("[X] Invalid option! Please choose a valid number.", "red")

def convert_image(input_path, output_path, output_format, log_file, syserr_path):
	try:
		print_colored(f"Processing: {input_path} -> {output_path}", "blue")

		if output_format == 'dds':
			convert_to_dds(input_path, output_path)
		elif output_format == 'tga':
			convert_to_tga(input_path, output_path)
		else:
			img = Image.open(input_path)

			if output_format == "webp":
				img.save(output_path, format="WEBP", quality=90)
			elif output_format == "ico":
				sizes = [(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)]
				img.save(output_path, format="ICO", sizes=sizes)
			elif output_format in ("jpg", "jpeg"):
				img.save(output_path, format="JPEG", quality=90)
			elif output_format == "bmp":
				img.save(output_path, format="BMP")
			else:
				img.save(output_path, format=output_format.upper())

		log_message(log_file, f"[OK] Converted: {input_path} -> {output_path}")
		print_colored(f"[OK] Successfully converted: {output_path}", "green")
		return True

	except Exception as e:
		err_msg = f"{input_path} -> {output_path} | {e}"
		log_message(log_file, f"[X] Error during conversion: {err_msg}")
		record_sys_error(syserr_path, err_msg)
		print_colored(f"[X] Error: {err_msg}", "red")
		return False

def main():
	input_folder  = "input"
	output_folder = "output"
	log_path      = "log.txt"
	syserr_path   = "syserr.txt"

	# Clear syserr.txt on each run
	open(syserr_path, "w", encoding="utf-8").close()

	if not os.path.exists(input_folder):
		print_colored(f"[X] Folder '{input_folder}' not found. Please create it and add images.", "red")
		return
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	input_format  = get_format_choice("Enter the initial format:")
	output_format = get_format_choice("Which format do you want to convert to:")

	start_time = time.time()
	files = [f for f in os.listdir(input_folder)
			if f.lower().endswith(f".{input_format}")]
	total_files = len(files)
	failed_images = []

	with open(log_path, "a", encoding="utf-8") as log_file:
		if total_files == 0:
			log_message(log_file, f"[X] No files with .{input_format} in '{input_folder}'.")
			print_colored(f"[X] No files with .{input_format} in '{input_folder}'.", "red")
		else:
			print_colored(f"Starting conversion of {total_files} file(s)...", "yellow")
			for file_name in files:
				in_path  = os.path.join(input_folder, file_name)
				out_file = os.path.splitext(file_name)[0] + f".{output_format}"
				out_path = os.path.join(output_folder, out_file)

				ok = convert_image(in_path, out_path, output_format, log_file, syserr_path)
				if not ok:
					failed_images.append(file_name)

	elapsed       = time.time() - start_time
	success_count = total_files - len(failed_images)
	percent       = int(success_count / total_files * 100) if total_files else 0

	final_msg = "\n" + "\n".join([
		f"Conversion from .{input_format} to .{output_format} completed:",
		f"  • Progress: {percent}% ({success_count}/{total_files} images)",
		f"  • Duration:  {elapsed:.2f} seconds"
	])
	if failed_images:
		failed_list = ", ".join(failed_images)
		final_msg += "\n" + f"  • Unconverted images: {failed_list} (details in syserr.txt)"

	print_colored(final_msg, "green")
	print("\nProcess finished. Press any key to exit.")

if __name__ == "__main__":
	main()
