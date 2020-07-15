import numpy as np
import pandas as pd
#new_cyclist_trials = np.array([[10,15,17,26,13,19],[12,13,14,24,14,23]])
#flatten the dataset
#x = new_cyclist_trials.ravel()
#print(type(x))
#print('*'*50)
#y = new_cyclist_trials.flatten()
#print(y)
#y = list(y)
#print(y)
#print(type(y))
#z = map(lambda n: n*5,y)
#a = list(z)
#print(a)
data = pd.DataFrame({'name': ['Willard', 'Al', 'Omar'],
'last': ['Morris','Jennings','Jennings']})

print(data.columns)
print(data.head())












