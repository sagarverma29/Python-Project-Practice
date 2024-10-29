class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self): #to print name and age
        return f"{self.name} {self.age}"
    def Function1(self): #method in class
        print(f"hello {self.name}")
Name1 = input()
Age1 = input()
obj = MyClass(Name1,Age1)
obj.Function1()