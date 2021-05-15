class Mobile:
    fp = 'yes'

    @classmethod
    def is_fp(cls):
        print("Finger Print:", cls.fp)


realme = Mobile()
redme = Mobile()
geek = Mobile()

print("Class FP:", Mobile.fp)
print("RealMe:", realme.fp)
print("Redmi:", redme.fp)
print("geek:", geek.fp)

Mobile.fp = 'No'
print("Class FP:", Mobile.fp)
print("RealMe:", realme.fp)
print("Redme:", redme.fp)
print("geek:", geek.fp)
print

realme.fp = 'Not Working'
print("Class FP:", Mobile.fp)
print("RealMe:", realme.fp)
print("Redme:", redme.fp)
print("gees:", geek.fp)





