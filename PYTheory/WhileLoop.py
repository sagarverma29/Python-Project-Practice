#1
i = 0 # initialization
while i<=10: # condition
    i+=1 # increment
    if i==5:
        break # if statement is true, the loop stops and exits.
    print(i)

#2
j=0
while j<10:
    j+=1
    if j==5:
        continue #if statement is true, it skips the iteration and continue 
    print(j)

#3
# table of 2
k=1
while k<=10:
    print(f"2 * {k} = {2*k}") # "f" is used to print variable 
    k+=1

#4
tuple1 = ("apple", "bananan", "cherry")
x=0
while x < len(tuple1):
    print(x) #returns address or indexes of the tuple
    print(tuple1[x]) #returns value of indexes in the tuple
    x+=1




