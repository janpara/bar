import MySQLdb

myDB = MySQLdb.connect(host="localhost",port=3306,user="usuario",passwd="usuario",db="parrillas")
cHandler = myDB.cursor()
cHandler.execute("SHOW DATABASES")
results = cHandler.fetchall()
for items in results:
    print items[0]