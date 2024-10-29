#From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.
def MyFunction(FN):
    print(FN)

#different ways to call function with arguments
#1
fn = "sagar"
MyFunction(fn)
#2
MyFunction("paji")
#3
MyFunction(FN="jolly")

#return 
#1
def func(num):
    return num*2
val = func(10)
print(val)
#2
def func2(num):
    return print(num*3) #directly return print statement
func2(20)

#3
def func3(num):
    result = []
    for x in num:
        result.append(2*x)
    return result
n = [1,2,3,4]
val1 = func3(n)
print(val1)

#If you do not know how many arguments that will be passed into your function, 
#add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly
#known as arbitary arguments