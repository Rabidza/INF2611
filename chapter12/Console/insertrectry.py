import sys
import mysql.connector as MySQLdb
from chapter12 import settings

try:
    conn = MySQLdb.connect(user=settings.USER, password=settings.PASSWORD,
                       host=settings.HOST, database=settings.DATABASE)
except:
    print("Error in establishing connection")
    sys.exit(1)

cursor = conn.cursor()
try:
    cursor.execute(
        """
        INSERT INTO products (prod_id, prod_name, quantity, price)
        VALUES(101, 'Camera', 100, 15)
        """
    )
    conn.commit()
    print("One row inserted into the products table")
except:
    conn.rollback()

cursor.close()
conn.close()