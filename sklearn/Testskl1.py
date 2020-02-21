import pandas as pd
import numpy as np
#loading inbuilt datasets
from sklearn.datasets import load_boston

#create an object to instantiate a dataset
boston_dataset = load_boston()

#built in methods to explore the dataset
print(boston_dataset['DESCR'])

#look into features in dataset
print(boston_dataset['feature_names'])

#store data in dataframe
df_boston = pd.DataFrame(boston_dataset.data)

#set features as columns in df
df_boston.columns = boston_dataset.feature_names

#view first observations
df_boston.head()

#print shape
print(boston_dataset.data.shape)
print(boston_dataset.target.shape)

#view target/response
print(boston_dataset['target'])

