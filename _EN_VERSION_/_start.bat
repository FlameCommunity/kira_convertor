@echo off
title Image Converter
cls

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
	echo [ERROR] Python is not installed or not added to PATH!
	echo Please install Python 3.8+ and try again.
	pause
	exit /b
)

:: Check if required modules are installed
python -c "import PIL, imageio, numpy" 2>nul
if %errorlevel% neq 0 (
	echo Missing dependencies detected. Installing required packages...
	pip install -r requirements.txt
)

:: Run the script
echo Starting the Image Converter...
python conv.py

:: Wait before closing
echo.
echo Process finished. Press any key to exit.
pause >nul
