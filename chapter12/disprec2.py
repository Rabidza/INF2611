import sys
import mysql.connector as MySQLdb
from chapter12 import settings

conn = MySQLdb.connect(user=settings.USER, password=settings.PASSWORD,
                       host=settings.HOST, database=settings.DATABASE)
cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM products")
    print("Product ID\tProduct Name\tQuantity\tPrice")
    rows = cursor.fetchall()
    for row in rows:
        print("%d\t\t\t%s\t\t\t%d\t\t\t%f" % (row[0], row[1], row[2], row[3]))
except MySQLdb.Error:
    print("Error in fetching rows")
    sys.exit(1)

cursor.close()
conn.close()
