import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Ameena&2808')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute('create database RUKSANA')