#Class Method w/o parameter
class Mobile:
    fp = 'Yes'          #Class Variable

    @classmethod
    def show_model(cls):
        print("Fingerprint:", cls.fp)

realme = Mobile()
Mobile.show_model()

#yhi istemal hai class method ka
#Now class method with parameter
class Mobile:
    fp = 'yes'

    @classmethod
    def show_model(cls, r):
        cls.ram = r
        print("RAM:", cls.ram)

realme = Mobile()
Mobile.show_model('4GB')
