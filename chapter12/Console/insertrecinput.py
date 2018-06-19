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

k = "yes"
while k.upper() == "YES":
    pid = int(input("Enter Product ID: "))
    pname = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))
    price = int(input("Enter Price: "))

    try:
        cursor.execute(
            """
            INSERT INTO products(prod_id, prod_name, quantity, price)
            VALUES(%d, '%s', %d, %f)
            """ % (pid, pname, qty, price))
        conn.commit()
        k = input("Want to insert more products, yes/no: ")
    except:
        print("Error inserting records")
        conn.rollback()
        sys.exit(1)

cursor.close()
conn.close()
