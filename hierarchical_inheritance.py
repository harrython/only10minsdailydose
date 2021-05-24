#herarical inheritance 
class Father:
    def showF(self):
        print("Father Class Method")

class Son(Father):
    def showS(self):
        print("Son Class Method")

class Daughter(Father):
    def showD(self):
        print("Daughter Class Method")

s = Son()
s.showS()
s.showF()


print()
print()
#agar apke pass constructor ho to
class Father:
    def __init__(self):
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Method")

class Son(Father):
    def __init__(self):
        super().__init__()              #calling super constructor
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Method")
class Daughter(Father):
    def __init__(self):
        super().__init__()              #baap ko call kar rhi hai mcd
        print("Daughter Class Constructor")
    def showD(self):
        print("Daughter Class Method")

s = Son()
d = Daughter()
