import mysql.connector
from mysql.connector import Error

class Consultas:

	#conn = mysql.connector.connect()
 
	# ^  Comentario temporal
	#* Metodo elimindo para ver si funcionan los metodos

	"""def __init__(self):
    		self.connectionDB()"""

	#& Method that connects to the db: 'quinielas'

	#@staticmethod		#! States that the method is static : Solve typeError for arguments,methods without 'self'
	def connectionDB(self):
		databasename = 'quinielas'
		user= 'apolorx'
		password = 'J0v3s4turn10-'
		host = 'localhost'
		try:
			conn = mysql.connector.connect(user=user,password=password,host=host,database=databasename)
			return conn
		except Error as e:
			return print(e)

	#& Method that finish the connection
	#@staticmethod
	def closeDB(self):
    		conn.close()

	#@staticmethod
	def returnResulsetStatistics(self):

			#Generates the connection to the database

			connec=self.connectionDB
			cursor = connec.cursor()
			cursor.execute("SELECT * FROM partidos")
			resultados = cursor.fetchall()
   
			for x in resultados:
				print(x)
    
			connec.close()
   
	
 # todo: Comentarios temporales para probrar los metodos 
class tools:

	c=Consultas()
 
	c.returnResulsetStatistics()

