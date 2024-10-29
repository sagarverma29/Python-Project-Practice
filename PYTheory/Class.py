# class always start with capital letter
#self is current instance of a class
#The __init__() function is called automatically every time the class is being used to create a new object.
class MyClass:
    def __init__(self,name,age): 
        self.name = name
        self.age = age
    def __str__(self): #to print name and age
        return f"{self.name} {self.age}"
    def Function1(self): #method in class
        print(f"hello {self.name}")

obj1 = MyClass("sagar",24)
print(obj1)
obj1.Function1()
obj2 = MyClass("paji",25)
print(obj2)
obj2.Function1()
print(type(obj1)) #type of object
print(type(obj2)) #type of object
