"""This will handle connection to database"""
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        user="root",
        password="",
        host="127.0.0.1",
        database="fastapi_demo",
        port=3306
    )