from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#Series
ser = Series([4, 7, -5, 3])
print(ser)


#we can see index on the left and the values on the right. 
# Since we did not specify an index for the data, a default
#consisting of the integers 0 through N - 1 (where N is the length of the data) is created.
#You can get the array representation and index object of the Series via its values
#and index attributes, respectively.
print(ser.values)
print(ser.index)

#to create a Series with an index identifying each data point
ser2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
ser2.index
print(ser2.index)
#manipulating and accessing values of series
ser2['a']
ser2['d'] = 6
ser2[['c', 'a', 'd']]

#NumPy array operations, such as filtering with a boolean array, 
# scalar multiplication,
#or applying math functions, preserve the index-value link
ser2
ser2[ser2 > 0]
ser2 * 2
np.exp(ser2)
#Note the unchanged index values

#Series is a fixed-length, ordered dict, as it is a mapping of index values 
# to data values.
'b' in ser2
'e' in ser2

#If you have data contained in a Python dict, you can create a Series from it by passing the dict:
sdata = {'paris': 35000, 'germany': 71000, 'greece': 16000, 'norway': 5000}
ser3 = Series(sdata)
print(ser3)

#When only passing a dict, the index in the resulting Series will have the 
# dict’s keys in
#sorted order
country = ['greece', 'paris', 'germany', 'norway']
ser4 = Series(sdata, index=country)
print(ser4)

#The isnull and notnull functions in pandas should be used to detect missing data
pd.isnull(ser4)
pd.notnull(ser4)

#Series also has these as instance methods
ser4.isnull()

#A critical Series feature for many applications is that it automatically 
# aligns differently indexed
#data in arithmetic operations:
ser3
ser4
ser3 + ser4

#Both the Series object itself and its index have a name attribute, which integrates with
#other key areas of pandas functionality:
ser4.name = 'population'
ser4.index.name = 'country'
ser4

#A Series’s index can be altered in place by assignment
ser.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
ser









