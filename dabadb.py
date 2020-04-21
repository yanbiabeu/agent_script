import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", passwd="school1")

print(mydb)

if (mydb):
	print("connection Successful")
else:
	print("connection not successfull")
