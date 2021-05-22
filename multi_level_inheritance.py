# Multi level inheritance
class Father:
    def showF(self):
        print("Father Class Method")

class Son(Father):
    def showS(self):
        print("Son Class Method")

class GrandSon(Son):
    def showG(self):
        print("GrandSon Class Method")

g = GrandSon()
g.showF()
g.showS()
g.showG()


class Father:
    def __init__(self):
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Method")

class Son(Father):
    def __init__(self):
        super().__init__()              #ab yeh apne baap ko bula rha hai
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Method")

class GrandSon(Son):
    def __init__(self):
        super().__init__()           #calling super class abe apne baap ko call kr rha hai
        print("GrandSon Class Constructor")
    def showG(self):
        print("GrandSon class Method")

s= GrandSon()

