import pandas as pd
data = [[1,2,3],[4,5,6],[7,8,9]]
row_labels = [1,2,3]
column_lables = ['A','B','C']

df = pd.DataFrame(data= data, columns= column_lables, index= row_labels) #to create a dataframe
print(df)
print(type(df)) #type of dataframe

#set_index
# print(df.set_index('C', drop= True)) #drop=true, drops column from DF 
# print(df.set_index('C', drop= False)) #drop=false, keeps the column and index in the DF
# print(df) #the DF is not updated, for that we use inplace=True
df.set_index('C', drop= False, inplace=True)
# print(df)
df.set_index('B', drop=False, inplace=True, append=True) #appends the column to existing index
print(df)

#reset_index
df.reset_index(drop=True, inplace=True)
print(df)