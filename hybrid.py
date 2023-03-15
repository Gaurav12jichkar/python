


class parent:
    def parent1(self):
        print("gaurav")

class child(parent):
    def child11(self):
        print("jichkar")

class child2(child1):
    def child22(self):
        print("i am 20 year old")

class child3(child,parent,child2):
    def child33(self):
        print("am bca grauate")
c=child3()
c.child11()
c.child22()
c.child33()
c.parent1()
       