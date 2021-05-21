#jab constructor ka behaviour change karna ho to constructor overriding use hota hai
class Father:
    def __init__(self):
        self.money = 100
        print("Father Class Constructor")

    def show(self):
        print("Father Class Inststance Method")


class Son(Father):
    def __init__(self):
        self.money = 5000000
        self.car = 'morchae car'
        print("Son Class Constructor")

    def disp(self):
        print("Son Class Instance Method")

s = Son()
print(s.money)
print(s.car)
s.disp()
s.show()

