import MySQLdb

myDB = MySQLdb.connect(host="janserver",port=3306,user="root",passwd="f1password")
cHandler = myDB.cursor()
cHandler.execute("SHOW DATABASES")
results = cHandler.fetchall()
for items in results:
    print items[0]