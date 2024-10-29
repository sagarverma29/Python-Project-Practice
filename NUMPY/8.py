#Array manipulation
# ARRAY RESHAPE
import numpy as np
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([[1,2,3,4,5],[9,8,0,6,5],[6,4,2,7,9]])

#reshape array into (2,3) matrix
print(np.reshape(arr1,(2,3)))
print(arr1.reshape(2,3)) #using reshape as a method
print("\n")

# ARRAY FLATTEN
print(np.ndarray.flatten(arr2)) #converted to 1D array
print(np.ndarray.flatten(arr2).shape) #shape shows it to be 1D array.
print("\n")

#ARRAY RAVEL
print(np.ravel(arr2)) 
print(arr2.ravel()) #calling as a method