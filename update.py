import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Ameena&2808',database='RUKSANA')
cur=mydb.cursor()
x='update SWAP set salary=salary+100 where emp_id=100'
cur.execute(x)
mydb.commit()