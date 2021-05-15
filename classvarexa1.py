#Exa for class variable

class Mobile:
    fp='yes'  # class variable

    @classmethod  #access karne k liyw class method ki jarurat hoti hia
    def is_fp(cls):
        print(cls.fp)  #Accessing the class variable inside the method

redmi=Mobile()
print(Mobile.fp)   #class k bahr wala call hua hai

Mobile.is_fp()   #calling inside
