# Nested Class in python

class Army:                             #Outer Class
    def __init__(self):
        self.name = 'Rahul'
        self.gn = self.Gun()            #Creating inner object 

    def show(self):
        print("Name:", self.name)

    class Gun:
        def __init__(self):
            self.name = 'AK 47'
            self.capacity = '75 Rounds'
            self.length = '34.3 In'

        def disp(self):
            print("Gun Name:", self.name)
            print("capacity:", self.capacity)
            print("Gun Length:", self.length)

a = Army()
print(a.name)
a.show()
print(a.gn.name)

g = a.gn                    # g = Army().Gun() inner class ka object banana ho to
print

print(g.name)
print(g.capacity)
print(g.length)
print()

g.disp()



