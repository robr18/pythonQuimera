import mysql.connector
from mysql.connector import Error

class Consultas:

	def __init__(self):
    		self.connectionDB()

	#& Method that connects to the db: 'quinielas'

	def connectionDB(self):
		conn= None
		databasename = 'quinielas'
		user= 'apolorx'
		password = 'f3b0ap0110'
		host = 'localhost'
		try:
			conn = mysql.connector.connect(user=user,password=password,host=host,database=databasename)
			if conn.is_connected():
				return print("Connected to BD")
		except Error as e:
			return print(e)
		conn.close()

class tools:

	c=Consultas()
