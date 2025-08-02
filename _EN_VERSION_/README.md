Image Conversion Script - Description & Installation Guide

Overview
This script allows image conversion between various formats, including PNG, JPG, DDS, TGA, WEBP, ICO and BMP. The script scans an input folder, processes the images, and saves them into an output folder, while generating a log of the conversion results. It also provides user interaction for format selection.

Features
✅ Conversion between PNG, JPG, DDS, TGA, WEBP, ICO and BMP  
✅ Uses texconv.exe for DDS conversion  
✅ Generates logs for each conversion  
✅ Allows interactive format selection  
✅ Automatically creates the required output folder

Installation & Setup
Step 1: Install Required Dependencies
Make sure you have Python 3 installed. You also need these Python libraries.

Install required modules
Run the following command in your terminal or command prompt:

pip install pillow imageio numpy


Step 2: Download texconv.exe (Required for DDS conversion)
If you plan to convert images to DDS format, download and place texconv.exe in the same directory as the script.

Download texconv.exe here: https://github.com/Microsoft/DirectXTex/releases  
After downloading, copy texconv.exe into the same folder where you have conv.py.

Usage Instructions
Step 1: Prepare the Files
Create a folder named `input` in the script’s directory. Place the images you want to convert into this folder.

Step 2: Run the Script
Run the script using the command:

python conv.py


Step 3: Select the Formats
When running, the script will ask:
- The input file format.
- The desired output format.
Enter the corresponding number for the format you want.

Step 4: Check Converted Files
Converted images will be saved in the `output` folder. The conversion log will be saved in `log.txt`.

Troubleshooting (Troubleshooting)
Common Errors & Solutions
❌ Error: texconv.exe not found  
✔ Solution: Make sure texconv.exe is placed in the script folder.

❌ Error: [X] Folder 'input' not found!  
✔ Solution: Create a folder named `input` and add your images.

❌ Error: [X] No files with extension .xxx in 'input'  
✔ Solution: Verify that you placed images in the `input` folder and selected the correct format.

Additional Notes
Avoid modifying sections marked with "DON'T TOUCH IF YOU DON'T KNOW WHAT YOU ARE DOING". The script supports conversion between .PNG, .JPG, .TGA and .DDS. The conversion process uses Pillow for most formats and texconv.exe for DDS.  
🚀 You’re now ready to start converting images! 🚀

This Python script has been updated to support conversion of images to and from ICO format, in addition to the existing formats: PNG, JPG, DDS, TGA, WEBP, ICO and BMP.

Main features:
📂 Automatic conversion of all files in a specified folder.  
🎨 Support for PNG, JPG, DDS, TGA, WEBP, ICO and BMP.  
📝 Automatic logging of all conversions and errors to a `log.txt` file.  
🔄 Fast processing and user-friendly interface with colored terminal messages.  
⚡ Conversion of WEBP files to other formats and vice versa, with a default quality setting of 90 for WebP.  
Now you can easily convert images between multiple formats, including WEBP, using this simple and efficient script. 🚀

------------------------------------------------------------------------------------------------------------------------------------------------
[UPDATE]
`syserr.txt` file  
– Records every error encountered during conversion (source → destination path and error message).  
– Automatically cleared at the start of each run.

Final message (“EndTask”)  
– Displays the total number of images processed and the success rate, e.g. 25/25 (100%).  
– If one or more conversions fail, details are listed in `syserr.txt` and full error entries in `log.txt`.

`log.txt` file  
– Maintains a detailed record for each file processed: timestamp, status ([OK] or [X]), source and destination paths, plus exception messages.

Auto‐clear of `syserr.txt`  
– On each script start, `syserr.txt` is cleared to begin with a fresh error log.

Colored console output  
– State messages displayed in different colors (blue for processing, green for success, red for errors, yellow for announcements).

DDS, TGA and BMP conversion  
– Direct support for exporting to TGA (using `imageio`), DDS (via `texconv.exe`) and BMP (via PIL), alongside PNG, JPG, WEBP and ICO.

Interactive format selection  
– Console menus for choosing input and output formats by number.

Total duration calculation and display  
– Times the entire process and shows the elapsed seconds at the end.

Automatic input file scanning  
– Scans the `input` folder for all images with the chosen extension and processes the batch without manual intervention.
------------------------------------------------------------------------------------------------------------------------------------------------
