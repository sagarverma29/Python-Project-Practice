#ARRAY CREATION FUNCTIONS
# FULL function
import numpy as np
print(np.full((2,5),1))
print("\n")

# ARANGE function
print(np.arange(1,20,3))
print("\n")

# LINSPACE function
print(np.linspace(1,50,num=20))
print(np.linspace(1,50,num=20).reshape((4,5))) #can reshape into any shape
print("\n")

# Random
print(np.random.rand(2,3))
print(np.random.randint(-10,20,(2,3)))
print("\n")

# Identity matrix
print(np.identity(3))
print("\n")

# zeros and ones
print(np.zeros((2,3),order="c"))
print(np.ones((2,3),order="C"))

