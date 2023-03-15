import mysql.connector
gaurav=mysql.connector.connect(host="localhost",user="Gaurav",password="Gaurav@12",database="gaurav")
print(gaurav)
a=gaurav.cursor()
print(a)
try:
    dataconnect=a.execute("select * from student where id=134")
    data=a.fetchall()
    print("name   id   rollno   address")
    for row1 in data:
        print("%s   %d   %d   %s",(row1[1],row1[1],row1[2],row1[3],row1[4]))
except:
    gaurav.rollback()