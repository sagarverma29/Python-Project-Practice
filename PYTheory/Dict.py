# # A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# # duplicate keys are allowed, but not values.
# #1
# dict1 = {
#     "name" : "sagar",
#     "age" : 25
# }
# print(dict1)
# print(type(dict1)) #returns type of the dictionary
# print(dict1.keys()) #prints all the keys present in the dictionary
# print(dict1.values()) #prints all the values in the dictionary
# print(dict1.items()) #returns a list of keys and values in a tuple
# print(dict1["age"]) #prints value of the key
# print(dict1.get("age")) #get function is also used to call value of key
# print(len(dict1)) # get length of dictionary

# #2
# # dictionary keys can have values in different types
# dict2 = {
#     "name": "mansimar",
#     "age": "24",
#     "hobbies": ["gaming","smoking"] # key contains value in list(can also be tuple/set)
# }
# print(dict2)
# print(dict2["hobbies"][1]) #to print a specific value from the list

# #3
# #using dict as a constructor
# dict3 = dict(
#     name = "sanskar",
#     age = 45,
#     hobbies = ["charlie", "noob"]
# )
# print(dict3)
# dict3["sex"] = "male" # to add a key and value in a dictionary
# dict3["age"] = 25 #to change the vaue of the key
# print(dict3)
# #dict3.pop("age") #delete the key and value mentioned
# #dict3.popitem() #deletes the last key and value in the dictionary

# #to make a copy of the dictionary into another variable
# mydict = dict3.copy()
# print(mydict)

# NESTED Dictionary
myFamily = {
    "child1" : {
        "name": "ABC",
        "year": 2000
    },
    "child2": {
        "name": "XYZ",
        "year": 2002
    }
}
print(myFamily)
# another way to write the same logic
friend1 = {
    "name": "Jolly",
    "age": 25
}
friend2 = {
    "name": "paji",
    "age": 24
}
myFriends = {
    "friend1" : friend1,
    "friend2" : friend2
}
print(myFriends)






