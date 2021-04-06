import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="apolorx",
  password="J0v3s4turn10-",
  database="quinielas"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM partidos")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)