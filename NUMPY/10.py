# Array manipulation
#ARRAY SORT
import numpy as np
arr1 = np.array([[10,4,99],[2,55,3],[8,77,64]])
print(np.sort(arr1, axis=0)) # sort array column wise
print("\n")
print(np.sort(arr1, axis=1)) # sort array row wise