import mysql.connector
con=mysql.connector.connect(host="localhost",user="Gaurav",password="Gaurav@12",database="gaurav")
cur=con.cursor()
try:
    cur.execute("update employee set name='ram' where id=4")
   
    con.commit()
    print("done")
except:
    con.rollback()

con.close()    