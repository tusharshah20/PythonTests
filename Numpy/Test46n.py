import numpy as np
new_cyclist_trials = np.array([[10,15,17,26,13,19],[12,13,14,24,14,23]])
#flatten the dataset
print(new_cyclist_trials.ravel())

#reshaping dataset
print(new_cyclist_trials.reshape(3,4))

#resize
print(new_cyclist_trials.resize(2,6))

#split array into 2
print(np.hsplit(new_cyclist_trials,2))

new_cyclist_1 = [10,15,17,26,13,19]
new_cyclist_2 = [12,13,14,24,14,23]

#stack the arrays together
print(np.hstack([new_cyclist_1,new_cyclist_2]))



