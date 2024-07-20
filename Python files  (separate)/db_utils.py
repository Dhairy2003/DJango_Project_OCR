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
        if connection.is_connected():
            print("Successfully connected to MySQL")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_tables(connection):
    cursor = connection.cursor()
    try:
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
        print("Tables created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating tables: {err}")
    finally:
        cursor.close()

def insert_aadhar_data(connection, phone_number, district, state):
    cursor = connection.cursor()
    try:
        cursor.execute("""
        INSERT INTO aadhar_data (phone_number, district, state)
        VALUES (%s, %s, %s)
        """, (phone_number, district, state))
        connection.commit()
        print("Aadhar data inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error inserting Aadhar data: {err}")
        connection.rollback()  # Rollback on error
    finally:
        cursor.close()

def insert_pan_data(connection, pan_number, name, dob):
    cursor = connection.cursor()
    try:
        cursor.execute("""
        INSERT INTO pan_data (pan_number, name, dob)
        VALUES (%s, %s, %s)
        """, (pan_number, name, dob))
        connection.commit()
        print("PAN data inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error inserting PAN data: {err}")
        connection.rollback()  # Rollback on error
    finally:
        cursor.close()

def close_connection(connection):
    try:
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed")
    except mysql.connector.Error as err:
        print(f"Error closing connection: {err}")
