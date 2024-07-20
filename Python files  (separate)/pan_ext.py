# pan_ext.py

import pytesseract
from PIL import Image
import re
import db_utils as db
from datetime import datetime

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# Specify the image path
image_path = '/Users/dhairyshrivastava/Desktop/VirtualEnvs/VisiOCR_1/VisiOCR_May_2024/OCR_DJango/Python files  (separate)/pan.png'

# Making PIL object
img = Image.open(image_path)

# Extract text from the image using Tesseract
extracted_content = pytesseract.image_to_string(img)

print("Extracted Content from PAN Card:")
print(extracted_content)

# Regular expressions for PAN card details
pan_number_pattern = r'[A-Z]{5}[0-9]{4}[A-Z]'
name_pattern = r'(?:Name|NAME):\s*(.*)'
dob_pattern = r'(?:DOB|Date of Birth):\s*(\d{2}/\d{2}/\d{4})'

# Find all matches in the extracted text
pan_numbers = re.findall(pan_number_pattern, extracted_content)
names = re.findall(name_pattern, extracted_content)
dobs = re.findall(dob_pattern, extracted_content)

print(f"Extracted PAN numbers: {pan_numbers}")
print(f"Extracted names: {names}")
print(f"Extracted dates of birth: {dobs}")

# Database insertion
connection = db.connect_to_mysql()
if connection:
    db.create_tables(connection)

    # Insert data only if all fields are extracted
    if pan_numbers and names and dobs:
        try:
            dob = datetime.strptime(dobs[0], '%d/%m/%Y').date()
            db.insert_pan_data(connection, pan_numbers[0], names[0], dob)
            print("PAN data inserted successfully.")
        except Exception as e:
            print(f"Error inserting PAN data: {e}")
    else:
        print("Incomplete data. Nothing to insert.")

    db.close_connection(connection)
else:
    print("Failed to connect to database.")
