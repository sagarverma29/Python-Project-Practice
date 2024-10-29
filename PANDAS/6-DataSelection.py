#DATA SELECTION
import pandas as pd
countires_sd = pd.read_csv(r'C:\Users\SAGAVERM\Desktop\DA dataset\top_10_countries.csv')
print(countires_sd)
#selecting data
print(countires_sd['Region']) #prints selcted column
print(countires_sd[['Region', 'Rank']]) #can slect multiple columns as list

#Iloc function 
print(countires_sd.iloc[1:2,1:5])
print(countires_sd.iloc[::-1]) #reverse a df

#Loc function
print(countires_sd.loc[2,'Region'])
print(countires_sd.loc[1:,['Country / Dependency','Region']])
print(countires_sd.loc[1:,'Country / Dependency':])

