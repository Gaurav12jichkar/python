class total:
    t=100
    def totalcal(self,sum):
        t=100
        if self.sum<100:
            print("the reamining ammout is:")
            print(t-self.sum)
        else:
            print("your are out of buget")
        
class bhavesh(total):
    print("bhavesh weekly expences")
    def be(self):
        sum=0
        a=1
        while a<=3:
            name=input("name of product you going to buy:")
            price=int(input("enter the price of product:"))
            sum=sum+price 
            a=a+1
        print("\t\t\t total week bill is:",sum)
    
        
class radhe(total):
    def re(self):
        print("radhe weekly expencese")
        bhavesh.be(self)
        

class akhilesh(total):
    def ae(self):
        
        print("akhilesh weekly expences")
        bhavesh.be(self)
    

class gaurav(total):
    def ge(self):
       print("gaurav weekly expences")
       bhavesh.be(self)
    
class rushi(total):
    def re(self):
       print("rushi weekly expences")
       bhavesh.be(self)
       
class abhishek(total):
    def ae(self):
        print("abhishek weekly expences")
            
b=bhavesh()
b.be()
b.totalcal(sum)
r=radhe()
r.re()
r.totalcal()
a=akhilesh()
a.ae()
# a.totalcal()
             



         



           
                                                      
        

  
