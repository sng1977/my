import mysql.connector

TestData = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="pds"
)

#mycursor = TestData.cursor()
#mycursor.execute("CREATE DATABASE my_first_db")

TestData = mysql.connector.connect(
     host="localhost",
     user="root",
     password="123",
     database="my_first_db"
 )

mycursor = TestData.cursor()
mycursor.execute("CREATE TABLE student (id int, name VARCHAR(255))")
mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary int(6))")
mycursor.execute("ALTER TABLE student MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("ALTER TABLE student ADD COLUMN address VARCHAR(255)")

mycursor = TestData.cursor()
sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
val = ("02", "John")
mycursor.execute(sql, val)
TestData.commit()

sql = "INSERT INTO employee (id, name,salary) VALUES (%s, %s, %s)"
val = ("01", "John", 10000)
mycursor.execute(sql, val)
TestData.commit()

mycursor = TestData.cursor()

sql = "INSERT INTO student (name, address) VALUES (%s, %s)"
val = [
    ('Николай', 'Киев, Гната Юріїє'),
    ('Сергей', 'Киев, Милютенка 23')
]
mycursor.executemany(sql, val)
TestData.commit()
print(mycursor.rowcount, "was inserted.")
