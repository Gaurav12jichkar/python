import mysql.connector
connection=mysql.connector.connect(host="localhost",user="Gaurav",password="Gaurav@12",database="gaurav")
print(connection)
a=connection.cursor()
sqlquery="insert into student(name,id,rollno,address) values(%s,%s,%s,%s)"
val1=[("radhe",1112,345,"panji"),("rae",1312,3345,"peenji")]
print(a)
try:
    dataconnect=a.executemany(sqlquery,val1)
   
    connection.commit()
    print(a.rowcount,"record inserted idno:",a.lastrowid)
    
except:
    connection.rollback()
