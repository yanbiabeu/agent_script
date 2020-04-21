import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="school1", database="webserver")

mycursor = mydb.cursor()

sql = "delete from employee where name='harshit'"

mycursor.execute(sql)

mydb.commit()
