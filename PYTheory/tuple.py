# A tuple is a collection which is ordered and unchangeable.
mtuple = ("a", "b", "c", "d")
print(mtuple)
print(type(mtuple)) #to print class of tuple

# convert tuple to list to change it
mlist = list(mtuple)
print(mlist)
print(type(mlist))
mlist.append("e") # append function to add element at the end of list
print(mlist)

# convert list to tuple post change another tuple
ntuple = tuple(mlist)
print(ntuple)
print(type(ntuple))
# convert list to tuple post change in original tuple
mtuple = tuple(mlist)
print(mtuple)

# adding element to tuple without converting
y = ("f", )
mtuple += y
print(mtuple)

# unpacking a tuple
(x,y,z,*p,q) = mtuple
print()
print(x)
print(y)
print(z)
print(p)
print(q)

# multi tuple
multiTuple = mtuple * 2
print(multiTuple)
