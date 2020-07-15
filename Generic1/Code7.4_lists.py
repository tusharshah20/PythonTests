#lists are variable-length and their contents can be modified
#[] or list()

a_list = [2, 3, 7, None]
tup = ('cool', 'bar', 'jazz')
b_list = list(tup)
a_list
b_list
type(a_list)
type(tup)
type(b_list)

numbers = [5,2,5,1,7,4]
numbers.append(100)
print(numbers)

numbers.insert(0,10)
print(numbers)

numbers.remove(5)
print(numbers)

#emptying list
numbers.clear()
print(numbers)

#removing element based on index
numbers = [1,5,2,5,1,7,4]
numbers.pop(4)
print(numbers)

#checking existence of a element
print(50 in numbers)

#find a count
print(numbers.count(5))

#sorting a list
numbers.sort() #shows none which is an object in python
print(numbers)

#sorting in descending order
numbers.reverse()
print(numbers)

#creating a copy 
#any operation on original list doesnt affect the copy
numbers2 = numbers.copy()

#concatenating and combining lists
newl = [4, None, 'foot'] + [7, 8, (2, 3)]
newl

#appending multiple elements to list i.e. entending a list
y = ['hello','cool',100]
newl.extend(y)
newl

#list concatenation is a compartively expensive operation since a new list must
#be created and the objects copied over. Using extend to append elements to an existing
#list, especially if you are building up a large list, is usually preferable.

#Slicing
seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[::2]

#pass -1 for reversing a list or tuple
seq[::-1]
