import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Ameena&2808',database='RUKSANA')
cur=mydb.cursor()
s='delete from SWAP where emp_id=103'
cur.execute(s)
mydb.commit()