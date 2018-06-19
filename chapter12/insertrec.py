import mysql.connector as MySQLdb
from chapter12 import settings

conn = MySQLdb.connect(user=settings.USER, password=settings.PASSWORD,
                       host=settings.HOST, database=settings.DATABASE)
cursor = conn.cursor()
cursor.execute(
    """
    INSERT INTO products(prod_id, prod_name, quantity, price)
    VALUES(101, 'Camera', 100, 15)
    """)

print("One row inserted into the products table")
cursor.close()
conn.commit()
conn.close()
