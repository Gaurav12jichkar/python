class gaurav:
    def msg(self):
        print("india is my contry")
        
class radhe:
    def msg1(self):
        print("but all indians are not my brother and sister")
        
class child(gaurav,radhe):
    def msg2(self):
        print("jay hind")
        
c=child()
c.msg()
c.msg1()
c.msg2()
            