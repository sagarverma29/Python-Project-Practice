# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
class Person: #parent class
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(f"hello {self.fname} {self.lname}")
class Student(Person): #child class
#The child's __init__() function overrides the inheritance of the parent's __init__() function. 
    def __init__(self, fname,mname, lname):
#super() function will make the child class inherit all the methods and properties from its parent:
        super().__init__(fname, lname) #super function is used to call/use parent class variables
        self.mname = mname
    def Printfull(self):
        print(f"Hi {self.fname} {self.mname} {self.lname}")
obj1 = Student("monkey","D","luffy")
obj1.printname()
obj1.Printfull()

