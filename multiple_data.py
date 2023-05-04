import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Ameena&2808',database='RUKSANA')
cur=mydb.cursor()
z= 'insert into swap(emp_id,emp_name,salary) values(%s,%s,%s)'
a=[(100,"GUSSA",10000),(102,"GUS",12000),(103,"GUSA",14000)]
cur.executemany(z,a)
mydb.commit()
print('data interested success')