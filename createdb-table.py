import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="school1", database="webserver")

mycursor = mydb.cursor()


mycursor.execute("Create table employee(name VARCHAR(200), sal int(20))")


