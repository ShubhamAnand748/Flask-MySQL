import mysql.connector

myDb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "emilence",
    database = "flask-mysqldb"
)
myCursor =  myDb.cursor()

try:
    print('Connection has been established successfully. \nConnection object is: {}'.format(myDb))
except:
    print('Unable to connect to the database.')
