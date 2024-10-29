# Higher order functions, eg: map, filter
# map 1 (using functions)
def square(x):
    return x**2
number = [1,2,3,4,5]
square_num = list(map(square,number))
print(square_num)
# map 2 (using lambda)
square_num = list(map(lambda x : x*x, number))
print(square_num)

# filter 1
even_num = list(filter(lambda x: x%2==0,number))
print(even_num) 