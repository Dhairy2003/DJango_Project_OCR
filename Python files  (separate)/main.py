# main.py

import os
import subprocess

# Define the base directory for the scripts
BASE_DIR = '/Users/dhairyshrivastava/Desktop/VirtualEnvs/VisiOCR_1/VisiOCR_May_2024/OCR_DJango/Python files  (separate)/'

def process_aadhar_card():
    script_path = os.path.join(BASE_DIR, 'aadhar_ext.py')
    if os.path.exists(script_path):
        subprocess.run(['/Users/dhairyshrivastava/Desktop/VirtualEnvs/VisiOCR_1/bin/python', script_path])
    else:
        print(f"Script not found: {script_path}")

def process_pan_card():
    script_path = os.path.join(BASE_DIR, 'pan_ext.py')
    if os.path.exists(script_path):
        subprocess.run(['/Users/dhairyshrivastava/Desktop/VirtualEnvs/VisiOCR_1/bin/python', script_path])
    else:
        print(f"Script not found: {script_path}")

def main():
    print("Welcome to Document OCR Processing")
    print("1. Process Aadhar Card")
    print("2. Process PAN Card")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        process_aadhar_card()
    elif choice == '2':
        process_pan_card()
    else:
        print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
