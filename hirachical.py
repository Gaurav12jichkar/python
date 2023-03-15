class parent:
    def parent(self):
        print("hello i am your dad")
class child1(parent):
    def child11(self):
        print("hello bc")
class child2(parent):
    def child22(self):
        print("hello mc")
class child3(parent):
    def child33(self):
        print("good byee")  

c=child1()
c.parent()
c.child11()
c1=child2()
c1.child22()
c1.parent()
c3=child3()
c3.child33()
c3.parent()  