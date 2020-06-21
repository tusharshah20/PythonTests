# # a = [1,2,3,4,5,6,7,8,8,9]
# # b = set(a)
# # b
# # a= [23,34,1,2,3,44,55,77,4,5,5,5,5,55,44,44,55]
# # b = set(sorted(a))
# # b
# # a
# # type(b)
# x = ('Helloworld')
# set(x)
possibleFeatures = ["storage","space","memory","cpu"]
featureRequests = ["i wish i had more storage","it would be good to have more cpu",
"i wish i had more memory","memory and cpu should be more","i need more storage",
"i need more cpu","i wish i had more memory","i wish i had more space"]
numFeatures = len(possibleFeatures)
print(numFeatures)
frlist = list(map(lambda n: n.split(),featureRequests ))
numFeatureRequests = len(frlist)
print(numFeatureRequests)
frlistCcat = []
for sublist in frlist: 
    for item in sublist:
        frlistCcat.append(item)
print(frlistCcat)
dictio = {}
newlist = []
for i in possibleFeatures:
    for j in frlistCcat:
        if i==j:
           m = i
           n = frlistCcat.count(i)
           dictio[m]=n

print(dictio)
newlist.append(dictio)
print(newlist)
print(type(newlist))


           
           






