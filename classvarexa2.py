#Class Variable or Static Variable with Class Method
class Mobile:
    fp = 'yes'                          #class variable

    def __init__(self):
        self.model = 'RealMe X'        #instance variable

    def show_model(self):              #instance method
        print("Model:",self.model)     #accessing instance var
    @classmethod
    def is_fp(cls):
        print("Finger Print:", cls.fp) #Accessing class variable inside method

realme = Mobile()
realme.show_model()

Mobile.is_fp()                         #Accessing class variable outside method
print()
Mobile.fp = 'No'
Mobile.is_fp()

#jab multiple objects hote hai to sare ek hi copy ko share karte hai
#ab hum yhi karenge 
