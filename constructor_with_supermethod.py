#How to call parent class constructor??
class Father:
    def __init__(self, m):
        self.money = m
        print("Father Class Constructor")           #ise bhi run karana hai to super method use kro

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self, m, j):
        super().__init__(m)                 #Parent class ko call kr rha hai
        self.job = j

        print("Son Class Constructor")

    def disp(self):
        print("Son Class Instance", self.money, self.job)

s = Son(1234567890987654321, 'python')
s.disp()
