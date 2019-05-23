import mysql.connector

def testconnection():
   print("testing connection..")
   mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="",
   database="instastalk"
   )
   print(mydb)

#def medialike(initiatorid, recepientid, mediaid, mediaurl):
def medialike(initiatorid, recipientid, mediaID, mediaURL):
   mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="",
   database="instastalk"
   )
   #Create user
   mycursor = mydb.cursor()
   sql = "INSERT IGNORE INTO user (instagramID) VALUES (%s),(%s)"
   val = (initiatorid,recipientid)
   mycursor.execute(sql,val)
   mydb.commit()
   mycursor.close()

   #Create media
   mycursor = mydb.cursor()
   sql = "INSERT IGNORE INTO media (instagramID, uploaderID, mediaURL) VALUES (%s,%s,%s)"
   val = (mediaID, recipientid, mediaURL)
   mycursor.execute(sql, val)
   mydb.commit()
   mycursor.close()

   #Create relationship
   mycursor = mydb.cursor()
   sql = "INSERT IGNORE INTO likes (userID, mediaID) VALUES (%s,%s)"
   val = (initiatorid,mediaID)
   mycursor.execute(sql, val)
   mydb.commit()
   mycursor.close()