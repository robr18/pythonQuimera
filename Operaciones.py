import mysql.connector
from mysql.connector import Error
import re

# REVIEW: Change this code to get the user and password from an external file and add it to .gitignore

conn = mysql.connector.connect(
	host = "localhost",
	user = "apolorx",
	password = "J0v3s4turn10-",
	database = "quinielas"
)

#REVIEW: Change that we get the total of jornadas from a global variable at the beggining of the file
# METHOD: Methot that returns the probability of an event, given two parameters (order and result)
def ProbabilityOfIndividualMatch(order,result):

		# SECTION: MySQL section: Matching the conditions and getting the total of cases
		cursor = conn.cursor()	 #PROCEEDURE[epic=mysql] Definition of cursor
		querie = "SELECT COUNT(idjorna) FROM partidos WHERE ordenJornada="+order+" AND resultado="+result	#PROCEEDURE: Querie that returns the numbers of jornadas that matches																#^ the conditions
		cursor.execute(querie)	#PROCEEDURE[epic=mysql] Execution
		result_condition = cursor.fetchone()	#PROCEEDURE: Return a resultset with the querie
		querie_total = "SELECT COUNT(distinct idjorna) from partidos"
		cursor.execute(querie_total)
		total_fields= cursor.fetchone()

		# SECTION: Statistical computing
		#! Parsing the total of cases and the matches that we got above
		events_happ= result_condition[0]

		total_r =total_fields[0]

		#PROCEEDURE: Obtaining the % of an event happening
		percentage_happenning = events_happ/total_r

		return float("%.17f"%percentage_happenning)


#METHOD Fill the table probindex with the stats of all the match's
#! EXECUTE ONLY ONCE IF TABLE 'probindex' is not filled
#REVIEW: Code that the method also creates the table probindex if it's not created
def insertIntoIndex():
		order=1
		cursor=conn.cursor()
		while order<=9:
			while result <= 2:
				prob_index = StatisticsOfIndividualMatch(str(order),str(result))
				insert_querie = ("INSERT INTO probindex(order_pi,result_pi,indexp)"
                     			"VALUES (%s,%s,%s)")
				data = (order,result,prob_index)
				try:
					cursor.execute(insert_querie,data)
					conn.commit()
					result+=1
				except:
					conn.rollback()
			order+=1

#METHOD Returns a list of id's of all the matchs of the conditions
def getIdJornada(order,result):
		cursor=conn.cursor()
		#If that controls if its the first querie for the algorithm or not
		querie_second= "SELECT idjorna FROM partidos WHERE ordenJornada="+str(order)+" AND resultado="+str(result)
		cursor.execute(querie_second)
		id_list=cursor.fetchall()
		return parseList(id_list)

#METHOD Iterates a list of ids with two parameters only
def IterateTroughList(id_list,order,result):
		list_temp=[]
		cursor=conn.cursor()
		for index in id_list:
			querie="SELECT idjorna FROM partidos WHERE idjorna=\""+str(index)+"\" AND ordenJornada="+str(order)+" AND resultado="+str(result)
			cursor.execute(querie)
			rs=cursor.fetchone()
			if rs:
				list_temp.append(rs[0])
		return 	list_temp

#METHOD Returns a list of ids that match multiple conditions
def getProbability(order,result):

		index=0
		length= len(order)
		id_list=[]
		while index<length:
			if(index!=0):
				id_list=IterateTroughList(id_list,order[index],result[index])
				index+=1
			else:
				id_list=getIdJornada(order[index],result[index])
				index+=1

		return id_list

#METHOD: Parse a list for getIndJornada()
def parseList(lista):
		listat= list(lista)
		lista_parse=[]
		for x in listat:
				lista_parse.append(parseString(x))
		return lista_parse

#METHOD: Parses a string from characters that generates errors from the fetchall() method of mysql
def parseString(string):
		temp=re.sub(r'\(|\)|\'|,',"",str(string))
		return temp

"""
def showJorna(id_list):
    
    	for x in id_list:
			"""


	#Statements to test the resulset of a querie
for x in getProbability([5,2,1,4],[1,2,1,1]):
    print(x)