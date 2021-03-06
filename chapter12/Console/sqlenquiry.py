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

p = int(input("Enter Product ID: "))
cursor.execute("SELECT * FROM products WHERE prod_id = %d" %p)
row = cursor.fetchone()
if row == None:
    print("Sorry no Product found with ID %d" %p)
else:
    print("Information of the product with id %d is as follows:" %p)
    print("Product ID: %d, Product Name: %s, Quantity: %d, Price: %f" % (row[0], row[1],
                                                                         row[2], row[3]))
cursor.close()
conn.close()
