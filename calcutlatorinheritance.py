a=50
b=5
class add:
    def addition(self):
        print(a+b)
        
class sub:
    def subtraction(self):
        print(a-b)
        
class mul:
    def multi(self):
        print(a*b)
 
class div(add,sub,mul):
     def division(self):
         print(a/b)


d=div()
d.addition()
d.subtraction()
d.multi()
d.division()

       
    
                