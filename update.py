import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="school1", database="webserver")

mycursor = mydb.cursor()

sql = "update employee set sal=70000 where name='ankita'"

mycursor.execute(sql)

mydb.commit()
