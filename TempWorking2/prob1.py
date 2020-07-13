# Problem statement
# You are working for a team and are trying to understand which features users want added
# to a new version of an app/device the most.Your team has received a large number of feature feature Requests
# from users.

# Write an algorithm that identifies the most popular N feature requests out of a list of feature requests &
# possible features. Your algorithm should output the most frequently mentioned features.

# Input:
# The input to the function/method consists of 5 arguements:
# numFeatures: an integer representing the number of possible features.
# topFeatures: an integer representing the number of top features that your function retuns (N)
# possibleFeatures: a list of single-word strings representing the possible features
# numFeatureRequests: an integer representing the number of feature requests.
# featureRequests: a list of strings where each element is a string that consists of space-separated words representing feature requests.

# Output:
# Return a list of strings representing the most popular N feature requests in order of most to least to least frequently mentioned.

# Note** the comparision of strings is case sensitive.
# If the value of topFeatures is  more than the number of possible features, return the names of
# only the features mentioned in the feature requests
# Multiple occurence of a feature in a quote should be considered as a single mention
# If features are mentioned an equal number of times in feature requests(eg:newshop=2,
# shownow=2,mymarket=4),sort alphabetically.topFeatures=2,Output=[mymarket,newshop]

# For example function can be:
# def popularFeatures(numFeatures, topFeatures, possibleFeatures,
#                     numFeatureRequests, featureRequests):
#     //write your code here
#     pass

# For example:
# Input:
# numFeatures=6
# topFeatures=2
# possibleFeatures=['storage','battery','disk','memory','waterresistent','processor']
# numFeatureRequests=7
# featureRequests=['I wish my device had more storage','I wish the battery life on 
# my device was good','I travel a lot and would enjoy if device was waterresistent',
# 'waterresistent and good processor are my two top requirements','I want to use 
# my device under water,waterresistent please Waterresistent!','How cool would it be if my device
# had strong processor']

# Output:
# [waterresistent,processor]
##################################################
#Solution Attempt
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


           
           






