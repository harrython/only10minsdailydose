#Exa 4. for more object creation important question

class Mobile:
    def __init__(self,m):
        self.model = m

    def show_model(self,p):
        self.price =p
        print("Model:", self.model, "Price:", self.price)

redmi = Mobile('Redmi note 7')   #jitne bhi objects haii unki apni separate mem
redmi.show_model(10000)         #allocate hogi
print(id(redmi))
print()

redi=Mobile('Redmi note 7 Pro')
redi.show_model(12000)
print(id(redi))
print()

geek=Mobile('Python')
geek.show_model(520)
print(id(geek))
print()




