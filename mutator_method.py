#yeh set bhi karega
#Instace Methods - Mutator Method/ Setter Method
class Mobile:
    def __init__(self):
        self.model = 'Note 7'

    def set_model(self):            #Mutator method
        self.model = 'Note 4'

realme = Mobile()
#Before Setting
print(realme.model)
#After Setting
realme.set_model()            #Calling Mutator Method
print(realme.model)
