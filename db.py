# db.py

import mysql.connector
import streamlit as st

def get_db_connection():
    try:
        conn = mysql.connector.connect(
             host="sql12.freesqldatabase.com",
            user="sql12727620",
            password="XAA48qmmxS",
            database="sql12727620"
        )
        return conn
    except mysql.connector.Error as err:
        st.error(f"Database Connection Error: {err}")
        return None
