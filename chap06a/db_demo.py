import mysql.connector


conn = mysql.connector.connect(
    user="root",
    password="",
    host="127.0.0.1",
    database="fastapi_demo",
    port=3306
)

# 2 techniques to db: 1. Query builder, 2. ORM
cursor = conn.cursor()

sql = "SELECT * FROM employee"
result = cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()