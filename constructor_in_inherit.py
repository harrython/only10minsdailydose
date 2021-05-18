# Constructor in inherit
# instance var inherit hota hai kaise yhi dekhna hai
class Father:
    def __init__(self, m):
        self.money = m
        print("Father Class Constructor")

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def disp(self):
        print('Son Class Instance Method', self.money+20)

s = Son(10)
print(s.money)
s.show()
s.disp()
                            #constructor k parameter ko kon pass karega argument-Child


