class one:
    def one1(self):
        print("hello ")

class two(one):
    def two2(self):
        print("how are you")

class three(two):
    def three3(self):
        print("lets starts the converation")

class four(three):
    def four(self):
        print("good by")
 
f=four()
f.one1()
f.two2()
f.three3()                      