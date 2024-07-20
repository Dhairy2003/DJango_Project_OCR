# aadhar_ext.py

import pytesseract
from PIL import Image
import re
import db_utils as db

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# Specify the image path
image_path = '/Users/dhairyshrivastava/Desktop/VirtualEnvs/VisiOCR_1/VisiOCR_May_2024/OCR_DJango/Image Inputs/2.png'

# Making PIL object
img = Image.open(image_path)

# Extract text from the image using Tesseract
extracted_content = pytesseract.image_to_string(img)

print("Extracted Content from Aadhar Card:")
print(extracted_content)

# Regular expression for extracting details
phone_number_pattern = r'Mobile:\s*(\d{10})'
district_pattern = r'District:\s*(\w+.*)'
state_pattern = r'State:\s*(\w+.*)'

# Find matches in the extracted text
phone_numbers = re.findall(phone_number_pattern, extracted_content)
districts = re.findall(district_pattern, extracted_content)
states = re.findall(state_pattern, extracted_content)

# Using first match or None if no match found
phone_number = phone_numbers[0] if phone_numbers else None
district = districts[0] if districts else None
state = states[0] if states else None

print(f"Extracted phone number: {phone_number}")
print(f"Extracted district: {district}")
print(f"Extracted state: {state}")

# Database insertion
connection = db.connect_to_mysql()
if connection:
    db.create_tables(connection)

    try:
        db.insert_aadhar_data(connection, phone_number, district, state)
        print("Aadhar data inserted successfully.")
    except Exception as e:
        print(f"Error inserting Aadhar data: {e}")

    db.close_connection(connection)
else:
    print("Failed to connect to database.")
