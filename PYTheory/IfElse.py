a = input()
b = input()

#if else normal method
if a>b:
    print("A")
elif a==b:
    print("=")
else:
    print("B")

#if else shorthand method
print("A") if a>b else print("=") if a==b else print("B")  

#nested if else
if a>b:
    print("A")
    if int(a)%2==0:
        print("even")
    else:
        print("odd")
elif a==b:
    print("=")
else:
    print("B")



