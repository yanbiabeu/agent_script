import mysql.connector
import sys
import os



class DataConnect:
	def __init__(self, host, password, database, user,):
		self.host = host
		self.password = password
		self.user = user
		self.database = database
		self.connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database)

	def Connection(self):
		self.dataCursor = self.connection.cursor()

	def ReadData(self):
		pass
con = DataConnect('localhost', 'school1', 'webserver', 'root')

 
print(self.connection)
print("""         *********************************
         *    Make your choice:          *
         *     1- Create database        *
         *     2- Create table           *
         *     3- Add entry to a database*
         *     4- Update entry in table  *
         *     5- delete entry           *
         *********************************""")


def rootCheck():
	if os.getuid() != 0:
		print("Error: You need root access")



 
