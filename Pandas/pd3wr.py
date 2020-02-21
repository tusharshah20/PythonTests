#Reshaping with Hierarchical Indexing
data = pd.DataFrame(np.arange(6).reshape((2, 3)),
index=pd.Index(['india', 'europe'], name='ctry'),
columns=pd.Index(['one', 'two', 'three'], name='number'))
data

#stack method on this data pivots the columns into the rows
result = data.stack()
result

#rearrange the data back into a DataFrame
result.unstack()
result.unstack(0)
result.unstack('ctry')

#if missing data introduced by unstacking
result.unstack().stack(dropna=False)

#long long to wide

