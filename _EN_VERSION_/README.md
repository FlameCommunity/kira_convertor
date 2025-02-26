Image Conversion Script - Description & Installation Guide Overview This script allows you to convert images between different formats, including PNG, JPG, DDS, and TGA. It scans an input folder, processes images, and saves them in an output folder while logging the conversion results. It also provides user interaction for selecting formats.

Features Converts PNG, JPG, DDS, and TGA images. Uses texconv.exe for DDS conversion. Generates logs for each conversion. Interactive format selection. Automatically creates the required output folder. Installation & Setup Guide Step 1: Install Required Dependencies Ensure you have Python 3 installed on your system. You will also need some Python libraries:

Install Required Python Modules Run the following command in the terminal or command prompt to install the necessary dependencies:

pip install pillow imageio numpy

Step 2: Download texconv.exe (Required for DDS conversion) If you plan to convert images to DDS format, you must download and place texconv.exe in the same directory as the script.

Download texconv.exe here: https://github.com/Microsoft/DirectXTex/releases Once downloaded, place texconv.exe in the same folder as conv.py.

Usage Instructions Step 1: Prepare Your Files Create a folder named input in the script directory. Place the images you want to convert inside the input folder. Step 2: Run the Script Run the script using the following command:

python conv.py

Step 3: Select Formats The script will prompt you to select:

The format of the input files. The desired output format. Choose the corresponding numbers when prompted.

Step 4: Check the Output The converted files will be saved in the output folder. Conversion logs will be saved in log.txt.

Troubleshooting Common Issues & Fixes 🔴 Error: texconv.exe not found ✔ Fix: Ensure texconv.exe is placed in the script folder.

🔴 Error: [X] Folder 'input' does not exist! ✔ Fix: Create a folder named input and place your images inside.

🔴 Error: [X] No files found with extension .xxx in 'input' ✔ Fix: Make sure you have placed images in the input folder and selected the correct input format.

Additional Notes Avoid modifying sections marked as "DON'T TOUCH IF YOU DON'T KNOW WHAT YOU ARE DOING". This script supports .PNG, .JPG, .TGA, and .DDS formats. The conversion process uses Pillow for most formats and texconv.exe for DDS. 🚀 Now you’re ready to start converting images! 🚀
