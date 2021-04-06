import mysql.connector
from mysql.connector import Error

class Consultas:

	conn = mysql.connector.connect()

	def __init__(self):
    		self.connectionDB()

	#& Method that connects to the db: 'quinielas'

	@staticmethod		#! States that the method is static : Solve typeError for arguments,methods without 'self'
	def connectionDB():
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

	#& Method that finish the connection
	@staticmethod
	def closeDB():
    		conn.close()

	@staticmethod
	def returnResulsetStatistics():

class tools:

	c=Consultas()

