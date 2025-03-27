import os
import subprocess
import datetime
from PIL import Image
import imageio
import numpy as np

# !!! NU ATINGE DACĂ NU ȘTII CE FACI !!! #
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
		raise FileNotFoundError(f"[X] texconv.exe nu a fost găsit în {texconv_path}. Asigură-te că se află în folderul scriptului.")

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
		"6": "ico"  # Suport adăugat pentru ICO
	}
	while True:
		print("\nSelectează formatul:")
		for key, value in format_options.items():
			print(f"{key} = {value}")
		choice = input(f"{message} ")
		if choice in format_options:
			return format_options[choice]
		print_colored("[X] Opțiune invalidă! Alege un număr valid.", "red")

def convert_image(input_path, output_path, output_format, log_file):
	try:
		print_colored(f"Se procesează: {input_path} -> {output_path}", "blue")

		if output_format == 'dds':
			convert_to_dds(input_path, output_path)
		elif output_format == 'tga':
			convert_to_tga(input_path, output_path)
		else:
			img = Image.open(input_path)

			if output_format == "webp":
				img.save(output_path, format="WEBP", quality=90)
			elif output_format == "ico":
				sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
				img.save(output_path, format="ICO", sizes=sizes)
			else:
				img.save(output_path, format=output_format.upper())

		log_message(log_file, f"[OK] Conversie reușită: {input_path} -> {output_path}")
		print_colored(f"[OK] Conversie reușită: {output_path}", "green")
	except Exception as e:
		log_message(log_file, f"[X] Eroare în timpul conversiei: {input_path} -> {output_path} | {e}")
		print_colored(f"[X] Eroare în timpul conversiei: {input_path} -> {output_path} | {e}", "red")

def main():
	input_folder = "input"
	output_folder = "output"
	log_path = "log.txt"

	if not os.path.exists(input_folder):
		print_colored(f"[X] Folderul '{input_folder}' nu există! Creează-l și adaugă imagini.", "red")
		return
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	input_format = get_format_choice("Introduceți formatul inițial: ")
	output_format = get_format_choice("În ce format dorești să convertești: ")

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
			log_message(log_file, f"[X] Nu s-au găsit fișiere cu extensia .{input_format} în '{input_folder}'.")
			print_colored(f"[X] Nu s-au găsit fișiere cu extensia .{input_format} în '{input_folder}'.", "red")

if __name__ == "__main__":
	main()
