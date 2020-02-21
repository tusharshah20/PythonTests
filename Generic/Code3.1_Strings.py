teststring = "earth is round"

#using built in functions
print(len(teststring)) #len is general purpose function


#using . operator to list methods(as in OOP)
#ie functions with specifically belong to smthing

print(
teststring.upper(),
teststring.lower(),
teststring.title(),
teststring.swapcase(),
teststring.startswith('r'))

#
print(teststring.upper())
print(teststring.lower())
print(teststring.title())
print(teststring.swapcase())
print(teststring.startswith('r'))
#
print(teststring.find('e')) #prints index of this element
print(teststring.replace('earth','Earth'))
print('Earth' in teststring)

#note: in show boolean value,find shows index



