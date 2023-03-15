student=input("enter the student name :")


studentdata={"bahvesh":90,"radhe":80,"shashank":70,"akhilesh":50}
def marks(student_name):
  for i in studentdata:
      if i==student_name:
          return studentdata[i] 
      
  else:
      return "there is no student"
    
          
print("marks of student",marks(student))    
    
    

