#ARRAY MANIPULATION
# ARRAY CONCATENATION
import numpy as np
arr1 = np.array([[1,1,1],[2,2,2]])
arr2 = np.array([[3,3,3],[4,4,4],[5,5,5]])
arr3 = np.array([[6,6],[7,7],[8,8]])

print(np.concatenate((arr3,arr2),axis=1)) #for axis 1, no. of columns should be equal
print("\n")
print(np.concatenate((arr1,arr2),axis=0)) #for axis 0, no. of rows should be equal
print("\n")

# ARRAY TRANSPOSE
print(np.transpose(arr1)) #inverts the rows and columns in arr1
