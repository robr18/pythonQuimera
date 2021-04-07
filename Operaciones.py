import mysql.connector
from mysql.connector import Error

# REVIEW: Change this code to get the user and password from an external file and add it to .gitignore

conn = mysql.connector.connect(
	host = "localhost",
	user = "apolorx",
	password = "J0v3s4turn10-",
	database = "quinielas"
)


# METHOD: Methot that returns the probability of an event, given two parameters (order and result)
def ProbabilityOfIndividualMatch(order,result):

		# SECTION: MySQL section: Matching the conditions and getting the total of cases
		cursor = conn.cursor()	 #^ Definition of cursor
		querie = "SELECT COUNT(idjorna) FROM partidos WHERE ordenJornada="+order+" AND resultado="+result	#^ Querie that returns the numbers of jornadas that matches																#^ the conditions
		cursor.execute(querie)	#^ Execution
		result_condition = cursor.fetchone()	#^ Return a resultset with the querie
		querie_total = "SELECT COUNT(distinct idjorna) from partidos"
		cursor.execute(querie_total)
		total_fields= cursor.fetchone()

		# SECTION: Statistical computing
		#! Parsing the total of cases and the matches that we got above
		events_happ= result_condition[0]

		total_r =total_fields[0]

		#^ Obtaining the % of an event happening
		percentage_happenning = events_happ/total_r

		return float("%.17f"%percentage_happenning)


#METHOD Fill the table probindex with the stats of all the match's
#! EXECUTE ONLY ONCE IF TABLE 'probindex' is not filled
#REVIEW: Code that the method also creates the table probindex if it's not created
def insertIntoIndex():
		order=1
		cursor=conn.cursor()
		while order<=9:
			result=0
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

#print(ProbabilityOfIndividualMatch("1","0"))

"""
	#Statements to test the resulset of a querie
for x in StatisticsOfIndividualResults("1","0"):
    print(x)	"""