#pandas intro
import pandas as pd
index1 = [0,1,2,3,4]
data1 = [22,44,11,55,33]
x = pd.Series(data=data1, index=index1)
print(x)