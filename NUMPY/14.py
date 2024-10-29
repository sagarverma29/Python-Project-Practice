#IO functions
import numpy as np
#load.txt function
x =np.loadtxt(r'C:\Users\SAGAVERM\Downloads\Course+Resurces-Python+for+Data+Analysis+and+Visualization\Course Resurces-Python for Data Analysis and Visualization\07 NumPy\6 IO Functions\tfl-daily-cycle-hires.txt',delimiter =',', skiprows=1, usecols =(1))
print(x)
print(f'mean = {x.mean()}') #mean of all values
print(f'max = {x.max()}') #max of all values
print(f'min = {x.min()}') #min of all values
print(f'standard deviation = {x.std()}') 

#to save array in a file
np.savetxt(r'C:\Users\SAGAVERM\Desktop\txt_array', x)