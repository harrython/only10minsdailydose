#Multiple Inheritance
class Father:
    def __init__(self):
        super().__init__()                  #calling parent class constructor
        print("Father Class Constructor")   #father ka parent object hai
    def showF(self):
        print("Father Class Method")

class Mother:
    def __init__(self):
        super().__init__()                  #calling parent class constructor
        print("Mother Class Constructor")   #mother ka parent bhi object hi hai
    def showM(self):
        print("Mother Class Method")

class Son(Father, Mother):                  #2nd no wala pahle execute hoga
    def __init__(self):                     #object me constructor na hone se right ko call karta hai
        super().__init__()                  #calling parent class constructor
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Method")

s =Son()



        
