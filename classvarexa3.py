# Class Variable
class Mobile:
    fp = 'yes'                              #Class Variable

    @classmethod                            #Class Method
    def is_fp(cls):
        print("Finger Print:", cls.fp)      #Accessing Class Variable


realme = Mobile()
redmi = Mobile()
geek = Mobile()

print("RealMe:", Mobile.fp)
print("Redmi:", Mobile.fp)
print("geek:", Mobile.fp)
print()
Mobile.fp = 'No'                           #Modifying Class Variable
print("RealMe:", Mobile.fp)
print("Redmi:", Mobile.fp)
print("Geek:", Mobile.fp)

