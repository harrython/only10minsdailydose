#Passing Members of one class to anothor class
class Student:
    #Constructor
    def __init__(self, n, r):
        self.name = n
        self.roll = r

    #Instance Method
    def disp(self):
        print("Student name:", self.name)
        print("Student roll:", self.roll)

class User:
    #Static Method
    @staticmethod
    def show(s):
        print("User Name", s.name)
        print("User Roll:", s.roll)
        s.disp()


#Creating Object of Student Class
stu = Student('Harisen', 17201)

User.show(stu)                   #static method ko call karne k liye classname.methodname

