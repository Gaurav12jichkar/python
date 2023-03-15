import subprocess
import mysql.connector
with open("file2.txt","wb") as f:
    subprocess.check_call(["python","list.py"],stdout=f)