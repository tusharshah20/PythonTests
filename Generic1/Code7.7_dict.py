#using dictionaries (hash map or associative array)
#when we would want to work on data that 
# is as a key,value pair

empty_dict = {}
d1 = {'a' : 'some value',
      'b' : [1, 2, 3, 4]}
d1

d1[1] = 'a test'
d1

d1['b']
'b' in d1
d1.keys()
d1.values()
del d1[1]
d1
n = d1.pop('a')
n
d1

a1 = {'help':'world',10:20}
d1.update(a1)
d1

#
customer = {
    "name":"john",
    "age":"30",
    "is_verified":"True"}

#each key in dict should be unique
print(customer["name"])

#print(customer["bday"])
print(customer.get("name"))
print(customer.get("bday")) #shows None

#provide default value instead of None
print(customer.get("bday","jan 1st")) 

customer["name"] = "james"
print(customer["name"])

customer["birth date"] = "Jan 1 2000"
print(customer["birth date"])
print(customer)
print(customer.values())

#mapping keys to values
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""

for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
    print(output)


#using split
message = input("> ")
words = message.split(' ')
print(words)

#mapping special characters to say emojis
message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😒"
}

output = ""
for word in words:
    output += emojis.get(word) + ""
print(output)

#


