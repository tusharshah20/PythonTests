#Applying functions/mapping
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
index=['germany', 'austria', 'russia', 'sweden'])
frame
np.abs(frame)

f = lambda x: x.max() - x.min()
frame.apply(f)
frame.apply(f, axis=1)

def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f)

#Element-wise Python functions can be used, too. To compute a
#formatted string from each floating point value in frame. use applymap
format = lambda x: '%.2f' % x
frame.applymap(format)

#map method in series for element-wise function
frame['e'].map(format)

#Sorting & Ranking
#To sort lexicographically by row or column index, use the sort_index method
ser8 = Series(range(4), index=['d', 'a', 'b', 'c'])
ser8.sort_index()

#With a DataFrame, you can sort by index on either axis
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
columns=['d', 'a', 'b', 'c'])
frame.sort_index()
frame.sort_index(axis=1)
frame.sort_index(axis=1, ascending=False)

#sorting dataframe by values
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame
frame.sort_index(by='b')
frame.sort_index(by=['a', 'b'])

#Ranking
#Ranking is closely related to sorting, assigning ranks from 1 to all valid data points
# in an array. The rank methods for Series and DataFrame breaks ties by assigning
#each group the mean rank

ser10 = Series([7, -5, 7, 4, 2, 0, 4])
ser10.rank()

#Ranks can also be assigned according to the order they’re observed in the data
ser10.rank(method='first')
ser10.rank(ascending=False, method='max')

#DataFrame can compute ranks over the rows or the columns:
frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
'c': [-2, 5, 8, -2.5]})
frame
frame.rank(axis=1)


