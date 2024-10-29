#reversing an array 1D and nD
import numpy as np
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([[1,2,3,4,5],[9,8,0,6,5],[6,4,2,7,9]])
    
#reversing 1D array
print(arr1[::-1]) #prints array in reverse order
print("\n")
#reversing nD array rows
print(arr2[::-1,::])
print("\n")
#reversing nD array columns
print(arr2[::,::-1])