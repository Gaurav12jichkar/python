import mysql.connector
 
connection=mysql.connector.connect(host="localhost",user="Gaurav",password="Gaurav@12",database="gaurav")
print(connection)
b=connection.cursor()
sqlquery="insert into student(name,id,rollno,address) values(%s,%s,%s,%s)"
value1=("gagf",134,1111,"ngpur"),

print(b)
try:
    #dataconnect=b.execute("show databases")
    # dataconnect=b.execute("create table student(name varchar(20) not null, id int(20) not null primary key, rollno float not null )")
    # dataconnect=b.execute("alter table student add address varchar(20) not null")
    dataconnect=b.executemany(sqlquery,value1)
   
    connection.commit()
    print(b.rowcount,"record inserted idno:",b.lastrowid)
    
except:
    connection.rollback()


