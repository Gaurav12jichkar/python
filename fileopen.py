# file1=open("file.txt","w")
# file1.write("hello gaurav, rahim")
# if file1:
#     print("hello file .txt is present")
#cheak the file is present or not if not then create by using append function.
# file1=open("file5.txt","a")
# file1.write("hello gaurav")
# if file1:
#  print("hello file5 .txt is present lorem34")
#---------------------------------------
# read file 
# file1=open("file5.txt","r")
# file12=file1.read(5)
# print(file12)
#using for loop
# file1=open("file5.txt","r")
# for i in file1:
#     print(i)
#readlines and readline
# f=open("file5.txt","r")
# f2=f.readline()
# print(f2)
# f2=f.readlines()
# print(f2)
# tell function 
# --------------------------------
# rename  and remove function
# import os
# os.rename("file3.txt","file2.txt")
# os.remove("file.txt")
#-------------------
#dir maker s
import os
# os.makedirs("gauravjichkar")
# print(os.getcwd())
os.chdir("C:\\phython\\gaura")
cwd = os.getcwd()
print(cwd)