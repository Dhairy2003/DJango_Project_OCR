# db_utils.py

import mysql.connector

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sdnv13579",
            database="visiocr"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS aadhar_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        phone_number VARCHAR(20),
        district VARCHAR(255),
        state VARCHAR(255)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pan_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        pan_number VARCHAR(10),
        name VARCHAR(255),
        dob DATE
    )
    """)
    connection.commit()
    cursor.close()

def insert_aadhar_data(connection, phone_number, district, state):
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO aadhar_data (phone_number, district, state)
    VALUES (%s, %s, %s)
    """, (phone_number, district, state))
    connection.commit()
    cursor.close()

def insert_pan_data(connection, pan_number, name, dob):
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO pan_data (pan_number, name, dob)
    VALUES (%s, %s, %s)
    """, (pan_number, name, dob))
    connection.commit()
    cursor.close()

def close_connection(connection):
    if connection.is_connected():
        connection.close()
