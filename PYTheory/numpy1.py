# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy stands for Numerical Python.
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr)) 

#NumPy is used to work with arrays. The array object in NumPy is called ndarray.
#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, 
# and it will be converted into an ndarray

#array indexing
print(arr[0])
print(arr[0]+arr[2])
