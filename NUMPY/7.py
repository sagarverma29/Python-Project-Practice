#value assigning diff between list and array
import numpy as np
arr1 = np.array([2,3,4,6,7,8,33])
list1 = [9,4,6,2,1,0,4]
#slicing a list and assigning same value to all the elements
try:
    list1[:] = 10
    print(list1)
except:
    print('can only assign an iterable')
#silcing an array and assigning same value to all elements
arr1[:] = 20
print(arr1)