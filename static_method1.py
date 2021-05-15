#class ya object ki jarurat na ho
#Static Method w/o parameter
class Mobile:
    @staticmethod               #Decorator
    def show_model():           #static method
        print("Note 7")

realme = Mobile()
Mobile.show_model()             #Calling Static method

#Static Method with parameter
class Mobile:
    @staticmethod
    def show_model(m,p):                #static method
        model = m
        price = p
        print("Model:", model, "Price", price)

realme = Mobile()
Mobile.show_model('Note 7', 10000)
