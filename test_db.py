from database.mysql_connector import get_connection

def main():
    conn, cursor = get_connection()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("Tables in chinook:", tables)
    conn.close()

if __name__ == "__main__":
    main()
from database.mysql_connector import get_connection

conn, cursor = get_connection()
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()
print("Tables in chinook:", tables)
conn.close()

