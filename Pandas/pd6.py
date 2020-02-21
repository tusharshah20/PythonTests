#operations between dataframe and series
arr = np.arange(12.).reshape((3, 4))
arr
arr[0]
arr-arr[0] #example of broadcasting
arr

frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
index=['germany', 'austria', 'russia', 'sweden'])

frame
series = frame.loc['germany']
series

#arithmetic between DataFrame and Series matches the index of the Series
#on the DataFrame's columns, broadcasting down the rows
frame - series

#If an index value is not found in either the DataFrame’s columns or the Series’s index,
#the objects will be reindexed to form the union
series2 = Series(range(3), index=['b', 'e', 'f'])
frame+series2

#to broadcast over the columns, matching on the rows, use one of the arithmetic methods.
series3 = frame['d']
frame
series
frame.sub(series3, axis=0)