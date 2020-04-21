import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="school1", database="webserver")

mycursor = mydb.cursor()

sqlform = "insert into employee(name,sal) value(%s, %s)"

employees = [("harshit", 20000), ("admit", 30000), ("ankita", 40000), ]

mycursor.executemany(sqlform, employees)

mydb.commit()
