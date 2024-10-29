#read_csv() input function
import pandas as pd
countries = pd.read_csv(filepath_or_buffer=r'C:\Users\SAGAVERM\Downloads\Course+Resurces-Python+for+Data+Analysis+and+Visualization\Course Resurces-Python for Data Analysis and Visualization\09 Pandas\03 Introduction to DataFrames\top_10_countries.csv')
print(countries)
print('\n')
#for output without header
countries1 = pd.read_csv(filepath_or_buffer=r'C:\Users\SAGAVERM\Downloads\Course+Resurces-Python+for+Data+Analysis+and+Visualization\Course Resurces-Python for Data Analysis and Visualization\09 Pandas\03 Introduction to DataFrames\top_10_countries_no_header.csv', header= None)
print(countries1)
