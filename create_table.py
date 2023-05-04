import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Ameena&2808',database='RUKSANA')
cur=mydb.cursor()
t='create table SWAP(emp_id integer(5),emp_name varchar(20),salary integer(10))'
cur.execute(t)