#Integer indexing
#Working with pandas objects indexed by integers can have issues
ser = Series(np.arange(3.))
ser

#if we do
ser[-1] #label-based indexing or position-based is difficult

#but if non-integer index
ser2 = Series(np.arange(3.), index=['a', 'b', 'c'])
ser2[-1]

#if you have an axis index containing indexers, data selection with integers will 
# always be label-oriented
ser.loc[:1]

#where you need reliable position-based indexing regardless of the index type,
#we can use the iget_value method from Series 
# and irow and icol methods from DataFrame:
ser3 = Series(range(3), index=[-5, 1, 3])
#ser3.iget_value(2)
frame = DataFrame(np.arange(6).reshape(3, 2)), index=[2, 0, 1])
#frame.irow(0)


