def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
print("enter number: ")
n = input()
fact = factorial(int(n))
print(f"factorial of {n} = {fact}") 