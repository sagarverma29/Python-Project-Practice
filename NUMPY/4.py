#silcing and indexing
import numpy as np
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([[1,2,3,4,5],[9,8,0,6,5],[6,4,2,7,9]])
#silcing and indexing is similar to list 
print(arr1[1]) #prints 1 index or 2 position in the array
print(arr2[0][4]) # prints element at 1 row and 5 column

#slicing
print(arr1[1:4])
print(arr2)
print(arr2[0:2,1:5]) #before comma is the 0 axis or thr rows and after is the 1 axis or the columns
