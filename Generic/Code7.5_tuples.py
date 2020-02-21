#working with tuples (espescially using when we need
# unmodifiable list)
#note** tuples are immutable
numbers = (1,2,3,5,6)
print(numbers[0])

tup = 4, 5, 6
tup

#creating a tuple of tuples
nested_tup = (4, 5, 6), (7, 8)
nested_tup

#converting sequence/iterator to tuple
x = tuple([4, 0, 2])
x
type(x)

tup = tuple('hello world')
tup

#slicing in tuples
tup[0:2]
tup[1:]
tup[:1]
tup[:-1]
tup[-5:-1]

tup = tuple(['foo', [1, 2], True])
tup[2] = False

#'tuple' object does not support item assignment

tup[1].append(3)
tup

#concatenating tuples
xccat = (4, None, 'hello') + (6, 0) + ('world',)
xccat

#xccat1 = (4, None, 'hello') + (['hello':'world']) + ('world',) #throws error

#concatenating via multiplication
xccat2 = ('fool', 'barbie') * 4
xccat2

#unpacking tuples
tup = (1,2,3)
a,b,c = tup
a
b
c

#Similarly sequences with nested tuples can be unpacked
tup = 4, 5, (6, 7)
a, b, (c, d) = tup
d

