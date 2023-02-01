import mysql.connector

TestData = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="pds"
)

#mycursor = TestData.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")

TestData = mysql.connector.connect(
     host="localhost",
     user="root",
     password="123",
     database="mydatabase"
 )

#mycursor = TestData.cursor()
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), address VARCHAR(255))")

mycursor = TestData.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('Николай', 'Киев, Гната Юріїє'),
    ('Сергей', 'Киев, Милютенка 23')
]
mycursor.executemany(sql, val)
TestData.commit()
print(mycursor.rowcount, "was inserted.")