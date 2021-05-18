# Single inheritance
class Father:
    money = 1000000

    def show(self):
        print("Parent Class Instance Method")

    @classmethod
    def showmoney(cls):
        print("Parent Class class Method:", cls.money)

    @staticmethod
    def stat():
        a= 10
        print("Parent Class Static Method:", a)
        

class Son(Father):
    def disp(self):
        print("Child Class instance Method")

s= Son()                     #ab Son class object se parent class k member ko access kr sakte hai
s.disp()

s.show()
s.showmoney()
s.stat()
