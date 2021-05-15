#Class Method w/o parameter
class Mobile:
    @classmethod            #Decorator
    def show_model(cls):    #Class Method
        print("Redmi Note 7")

realme = Mobile()
Mobile.show_model()         #calling class method

#isme kuchh khas class method ka use nhi hua hai
#class method ka use class variable me use hota hai aksar
