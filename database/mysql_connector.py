import mysql.connector
from config.db_config import DB_CONFIG

def get_connection():
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],        # ✅ key
        user=DB_CONFIG["user"],        # ✅ key
        password=DB_CONFIG["password"],# ✅ key
        database=DB_CONFIG["database"] # ✅ key
    )
    cursor = conn.cursor(dictionary=True)
    return conn, cursor
