import pandas as pd
# dcitionary data type in pandas
dict1 = {1:'A', 2:'B', 3:'C', 4:'D'}
x = pd.Series(data=dict1, index= dict1) #same object can be passed in to the data and index field
# the above code can also be written in another way
y = pd.Series(dict1)
print(f"{x}\n{y}")
