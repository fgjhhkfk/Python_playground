from mysql.connector import MySQLConnection
from python_mysql_dbconfig import read_db_config


def read_db():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM temperature;")
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

read_db()
