# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators 
# with the same name that can be executed on many objects or classes.
class Vehicle: #parent class
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def move(self): #move function
        print("move")
class Car(Vehicle):
    pass #inhertits functions from the parent class
class Ship(Vehicle):
    def move(self): #polymorphisim 1
        print("sail")
class Plane(Vehicle):
    def move(self): #polymorphisim 2
        print("fly")
a = Car("santro",1999) #values to variable populated from parent class
b = Ship("yatch", 2015)
c = Plane("boeing", 2020)
for x in (a,b,c): #for loop to print brand, year and move function for objects a,b,c
    print(x.brand)
    print(x.year)
    x.move()

