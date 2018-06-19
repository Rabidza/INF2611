import sys
import mysql.connector as MySQLdb
from chapter12 import settings

conn = MySQLdb.connect(user=settings.USER, password=settings.PASSWORD,
                       host=settings.HOST, database=settings.DATABASE)
cursor = conn.cursor()

try:
    cursor.execute(
        """
        create table products(prod_id smallint NOT NULL,
        prod_name char(50),
        quantity smallint,
        price float)
        """
    )
except MySQLdb.Error:
    print("Error in creating products table")
    sys.exit(1)

cursor.close()
conn.close()
