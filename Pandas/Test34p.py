import numpy as np
import pandas as pd
#list being passed as an object
first_series = pd.Series(list('abcdef'))
print(first_series)

print('*'* 50)

np_country = np.array(['luxembourg','Norway','Japan','Switzerland','USA','Qatar'])
s_country = pd.Series(np_country)
print(s_country)

#evaluate countries and their corresponding gdp per capita and print them as series
dict_country_gdp = pd.Series([52056.1234,40345.4565,45456.78564,33245.56782,34544.45888],index=['Luxembourg','Japan','Norway',
'China','India'])
print(dict_country_gdp)

#print series with scalar input
scalar_series = pd.Series(5.,index = ['a','b','c','d','e'])
print(scalar_series)

#access elements in a series
print(dict_country_gdp[0])
#access first 3 countries from series
dict_country_gdp[0:3]
#Lookup a country by name or index
dict_country_gdp.loc['USA']
#Lookup by position
dict_country_gdp.iloc[0]

