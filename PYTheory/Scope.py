# A variable is only available from inside the region it is created. This is called scope.
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

#local variable
def func1():
    x = 300 # x is a local variable, since initialized inside, scope of fucntion
    print(x)
func1()

#global variable
y = 400 # y is a gloabal variable, since initialized outside of function scope
def func1():
    print(y)
func1()

# If you operate with the same variable name inside and outside of a function, Python will treat them as 
# two separate variables, one available in the global scope (outside the function) and one available 
# in the local scope (inside the function)
a = 100
def func2():
    a = 50
    print(a)
print("local variable: ")
func2()
print(f"global variable: \n{a}")

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
b = 20
def func3():
    global b 
    b = 10
    print(b)
func3()

# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.
def f1():
    z = "john"
    def f2():
        nonlocal z
        z = "sagar"
    f2()
    return z
print(f1())