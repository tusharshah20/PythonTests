import pandas as pd
import numpy as np
#series indexing 
ser7 = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
ser7
ser7['a']
ser7[1] 
ser7[1] == ser7['b']
ser7[2:4]
ser7[[1,3]]
ser7[ser7>2]

#Slicing with labels behaves differently than normal Python slicing in that the endpoint
#is inclusive
ser7['b':'c']

#setting values
ser7['b':'c'] = 5
ser7

#indexing into a DataFrame
data1 = DataFrame(np.arange(16).reshape((4, 4)),index=['paris', 'belgium', 'vienna', 'basel'],
columns=['one', 'two', 'three', 'four'])
data1

data1['two']
data1[['three','one']]
data1[:2]
data1[data1['three'] > 5]

#indexing with a boolean DataFrame
data1 < 5

data1[data1 < 5] = 0
data1

#For DataFrame label-indexing on the rows
data1
data1.loc['belgium',['two','three']]
data1.loc[['belgium', 'paris'], ['two','three']]
data1.loc[:'belgium','two']

#Arthimetic and Data Alignment
#arithmetic operation between objects with different indexes. When adding together objects, 
# if any index pairs are not the same, the respective index in the result will be the union of the index pairs.

s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1
s2
s1+s2

#In the case of DataFrame, alignment is performed on both the rows and the columns:
df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])

#Adding returns a DataFrame whose index and columns are the unions of the ones in each DataFrame:
df1+df2

#Arithmetic methods with fill values
df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df1+df2

#using add method
df1.add(df2, fill_value=0)

#when reindexing a Series or DataFrame, you can also specify a different fill value
df1.reindex(columns=df2.columns, fill_value=0)