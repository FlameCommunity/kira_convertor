Image Conversion Script - Description & Installation Guide
Overview
This script allows you to convert images between different formats, including PNG, JPG, DDS, and TGA. It scans an input folder, processes images, and saves them in an output folder while logging the conversion results. It also provides user interaction for selecting formats.

Features
Converts PNG, JPG, DDS, TGA and WEBP images.
Uses texconv.exe for DDS conversion.
Generates logs for each conversion.
Interactive format selection.
Automatically creates the required output folder.
Installation & Setup Guide
Step 1: Install Required Dependencies
Ensure you have Python 3 installed on your system. You will also need some Python libraries:

Install Required Python Modules
Run the following command in the terminal or command prompt to install the necessary dependencies:

pip install pillow imageio numpy

Step 2: Download texconv.exe (Required for DDS conversion)
If you plan to convert images to DDS format, you must download and place texconv.exe in the same directory as the script.

Download texconv.exe here:
https://github.com/Microsoft/DirectXTex/releases
Once downloaded, place texconv.exe in the same folder as conv.py.

Usage Instructions
Step 1: Prepare Your Files
Create a folder named input in the script directory.
Place the images you want to convert inside the input folder.
Step 2: Run the Script
Run the script using the following command:

python conv.py


Step 3: Select Formats
The script will prompt you to select:

The format of the input files.
The desired output format.
Choose the corresponding numbers when prompted.

Step 4: Check the Output
The converted files will be saved in the output folder.
Conversion logs will be saved in log.txt.

Troubleshooting
Common Issues & Fixes
🔴 Error: texconv.exe not found
✔ Fix: Ensure texconv.exe is placed in the script folder.

🔴 Error: [X] Folder 'input' does not exist!
✔ Fix: Create a folder named input and place your images inside.

🔴 Error: [X] No files found with extension .xxx in 'input'
✔ Fix: Make sure you have placed images in the input folder and selected the correct input format.

Additional Notes
Avoid modifying sections marked as "DON'T TOUCH IF YOU DON'T KNOW WHAT YOU ARE DOING".
This script supports .PNG, .JPG, .TGA, and .DDS formats.
The conversion process uses Pillow for most formats and texconv.exe for DDS.
🚀 Now you’re ready to start converting images! 🚀

--- NEWS ---
This Python script has been updated to support image conversion to and from WEBP format, alongside the existing formats: PNG, JPG, DDS, and TGA.

Main features:
📂 Automatic conversion of all files in a specified folder.
🎨 Support for PNG, JPG, DDS, TGA, and WEBP formats.
📝 Automatic logging of all conversions and errors in log.txt.
🔄 Fast processing and a user-friendly interface with colored terminal messages.
⚡ Converts WEBP files to other formats and vice versa, with a default quality setting of 90 for WebP.

----------- PREVIEW -----------
![Screenshot_43](https://github.com/user-attachments/assets/2beac4b5-f188-4a4a-a9a6-8a1bcd304fb0)
![Screenshot_44](https://github.com/user-attachments/assets/db9effe0-e399-4bcb-a7aa-7ee2a8e75d59)
![Screenshot_45](https://github.com/user-attachments/assets/c7e4f8c1-60f3-454c-8803-927c7ee68a00)
![Screenshot_46](https://github.com/user-attachments/assets/26eadbf7-de20-412d-a55f-4f9d6ad12449)
![Screenshot_47](https://github.com/user-attachments/assets/6ffad8b0-e30a-4a58-a096-fc419a875ea9)
