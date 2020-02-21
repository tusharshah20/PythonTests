import warnings 
from warnings import simplefilter
#ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)
import numpy as np
import pandas as pd
import sklearn
#print('sklearn: %s' % sklearn.__version__)
#import sklearn load dataset
# iris dataset was prepared -outlining structural differences between 3 
# species of iris flower
from sklearn.datasets import load_iris
iris_dataset = load_iris()

#type of dataset
type(iris_dataset)

print(iris_dataset.DESCR)

#view features
print(iris_dataset.feature_names)

#view target
print(iris_dataset.target)

#shape of dataset
print(iris_dataset.data.shape)

#Assign features to X axis
X_feature = iris_dataset.data

#assign target to Y-axis
Y_target = iris_dataset.target

print(X_feature.shape)
print(Y_target.shape)

#using KNN classifier method  to find nearest neaighbours of a data point 
# for a given value of K
# import KNN classifier class from sklearn neighbours
#object used to instatiate class for a learning model: estimator
from sklearn.neighbors import KNeighborsClassifier 

#passing k neighbour value=1 for estimator to look for first neartest neighbour
knn = KNeighborsClassifier(n_neighbors=1)

#knn object and its properties
print(knn)

#fit data into KNN model (estimator)
knn.fit(X_feature,Y_target)

#pass 2 new set of values to object for prediction
X_new = [[3,4,5,1],[5,3,4,5]]

#predict the outcome for the new observation using knn classifier
print(knn.predict(X_new))

print('*'*60)

#using logistic regression estimator
from sklearn.linear_model import LogisticRegression
logReg = LogisticRegression()

#fitting data into logistic regression estimator
logReg.fit(X_feature,Y_target)

#predit the outcome
print(logReg.predict(X_new))
