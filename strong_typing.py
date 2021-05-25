# Strong Typing
class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak")

class Cat:
    def talk(self):
        print("Meow Meow")

def myfunction(obj):            #walk name ka method hai to hi call kro
    if hasattr(obj, 'walk'):    #obj me walk method hai to True kar k dega
        obj.walk()
    if hasattr(obj, 'talk'):
        obj.talk()

d = Duck()
myfunction(d)

h = Horse()
myfunction(h)

c = Cat()
myfunction(c)
