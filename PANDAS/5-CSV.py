import pandas as pd
print(pd.options.display.max_rows) #shows the max rows system will generate
#in order to increase the number of max rows assign value to pd.options.display.max_rows

#the head function returns a specific number of rows from the top.
x = pd.read_csv(r'C:\Users\SAGAVERM\Desktop\DA dataset\top_10_countries.csv').head(5)
print(x, '\n')

#the tail function returns the header and the last 5 rowa in a dataset
y = pd.read_csv(r'C:\Users\SAGAVERM\Desktop\DA dataset\top_10_countries.csv').tail()
print(y)

# info() function returns information about the dataset
df = pd.read_csv(r'C:\Users\SAGAVERM\Desktop\DA dataset\top_10_countries.csv')
print(df.info())
df.describe()
