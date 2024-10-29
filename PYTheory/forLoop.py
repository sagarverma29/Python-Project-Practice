# #1
# str = "Hello"
# for x in str: # x is the increment variable
#     print(x)

# #2
# for x in range(6): #range function can also be defined as range(2,6)-> will print 2,3,4,5
#     print(x)

# #3
# L1 = [1,2,3,4]
# for x in L1:
#     pass #cannot leave for loop empty, 

# #4
# tuple1 = ("apple", "bananan", "cherry")
# for x in range(len(tuple1)):
#     print(x) #returns address or indexes of the tuple
#     print(tuple1[x]) #returns value of indexes in the tuple

#5
name = {
    "fname": "Sagar",
    "lname": "verma"
}
for n in name:
    print(n) #returns keys
    print(name[n]) #return values

for x in name.values(): #to directly return values
    print(x)

for m in name.items(): #returns keys and values
    print(m)

for k in name.keys(): #returns keys
    print(k)