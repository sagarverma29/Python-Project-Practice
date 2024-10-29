# A set is a collection which is unordered, unchangeable, and unindexed
mset1 = {"a","b","c","d"}
print(mset1)
print(type(mset1))

mset2 = {1,2,3,4,False,True,0} # false and 0 are same, true and 1 are same, 
print(mset2)                   # since there are no duplicates in set, only one will be accepted

# add element in set
mset1.add("e")
print(mset1)

#update set 
nset1 = {1,2,3,}
nset2 = {4,5,6,3}
nset1.update(nset2) #use update function
print(nset1)

# remove or delete element from a set
#using nset1
nset1.remove(2) # if the element mentioned is not present in set, it will throw an error
print(nset1)
nset1.discard(2) # doesnt matter if the element is present or not, no errror will be thrown
print(nset1)
#nset1.pop(),can also be used,but since sets are unorderd,a random element may be be removed from the end.
#nset1.clear(), to clear the set
# del nset1, to delete the set

# union operator
Setunion = nset1.union(nset2) #update operator updates the value of set, but does not let u store it in new variable.
print(Setunion)

#intersection operator
nset1.intersection_update(nset2) #for updating existing set
print(nset1)

kset1 = {2,5,4,6}
kset2 = {9,0,5,1}
kset3 = kset1.intersection(kset2)
print(f"\n{kset3}")
    
print(f"length is: {len(Setunion)}") #length of set
