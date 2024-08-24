# db_utils.py

import mysql.connector
import streamlit as st
from db import get_db_connection

def save_file_details(user_id, file_name, ipfs_link, encryption_key):
    conn = mysql.connector.connect(
        host="sql12.freesqldatabase.com",
            user="sql12727620",
            password="XAA48qmmxS",
            database="sql12727620"
    )
    cursor = conn.cursor()
    
    # Insert into the files table
    sql = "INSERT INTO files (user_id, file_name, ipfs_link, encryption_key) VALUES (%s, %s, %s, %s)"
    values = (user_id, file_name, ipfs_link, encryption_key)
    cursor.execute(sql, values)

    conn.commit()
    cursor.close()
    conn.close()
