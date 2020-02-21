import numpy as np

distance = [10,15,17,24]
time = [.30,.47,.55,1.20]
np_time = np.array(time)
np_distance = np.array(distance)
speed = np_distance/np_time
print(speed)
