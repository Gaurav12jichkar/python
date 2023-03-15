p=39
def demo():
    a=34
    b=34
    global p
    p=37
    c=a+p
    print("addition of a and b",c)
print("the fuction call") 
print(p)  
demo()
