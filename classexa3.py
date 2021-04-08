#Exa 3
class Mobile:
    def __init__(self,m):   #this is constructor
        self.model = m

    def show_model(self, p):
        price = p
        print("Model:", self.model, "Price:",price)


redmi= Mobile('Redmi Note 7')   # constructor ke pass chla jayega
redmi.show_model(10000)  # 10000$ p ke pass chla jayega

