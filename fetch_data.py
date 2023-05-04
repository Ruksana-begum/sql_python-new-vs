import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Ameena&2808',database='RUKSANA')
cur=mydb.cursor()
f='select * from Swap'
cur.execute(f)
display=cur.fetchall()
for x in display:
    print(x)