#sirf data ko access karta hai 
#Instance Method - Accessor Method/ Getter Method
class Mobile:
    def __init__(self):                  #instance variable
        self.model = 'Note 7'

    def get_model(self):                 #Accessor Method
        return self.model

realme = Mobile()
m=realme.get_model()
print(m)
