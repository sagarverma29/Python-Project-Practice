#boolean array indexing
import numpy as np
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([[1,2,3,4,5],[9,8,0,6,5],[6,4,2,7,9]])
print(arr1>3) #return bool values for the condition
#to print elements according to the condition
print(arr1[arr1>3]) #prints elements in array grater than 3, i.e filtered the array

#bool condition for nd array
print(arr2>3)
print(arr2[arr2>3]) #returns elements in 1D array

