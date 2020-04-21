import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="school1", database="webserver")

mycursor = mydb.cursor()
mycursor.execute("select * from employee")

myresult = mycursor.fetchall()

for row in myresult:
	print(row)

