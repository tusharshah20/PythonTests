import numpy as np
#broadcasting 
array_a = np.array([2,34,5,8])
array_b = np.array([.3,.3,.3,.3])

result = array_a * array_b
print(result)

#variable with a scalar value
scalar_c = 0.3

#multiple array with scalar value
result2 = array_a * scalar_c
print(result2)
