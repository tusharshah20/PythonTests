#K-Means using sklearn
#kmeans test
import numpy as np
#import KMeans class from sklearn.cluster
from sklearn.cluster import KMeans
#scikit has random sample generators
#import make_blobs dataset from sklearn.cluster
#they are used to create artifical datasets of a specified complexity n size

from sklearn.datasets import make_blobs

#specify property of dataset to be generated
#define number of samples
n_samples = 300 #defines total no of points distributed equally

#define random state value to intialize the cluster
random_state = 20 # to intialize the centroid

#define how many features the sample will have
X,y = make_blobs(n_samples=n_samples,n_features=5,random_state=None)

#define the number of clusters to be formed as 3 and fit features in model
predict_y = KMeans(n_clusters=3,random_state=random_state).fit_predict(X)

#if we print the estimator object, it returns lable value of each datapoint

print(predict_y)




