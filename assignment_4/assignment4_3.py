#(Machine Learning) Consider the file winequality-red.csv located in the folder Datasets.
# Design a Python program that will calculate the first 4 principal components of the data
    # with the exception of the variable quality.
#(a) What percentage of the variance is captured by the second principal component?
#(b) What are the coordinates of the second principal vector?

import pandas as pd
from sklearn.decomposition import PCA
import numpy as np

filepath = '/Users/andrewtran/Documents/pycharm/5003/assignment_4/winequality-red.csv'
data = pd.read_csv(filepath)
print(data.head())

newdata = data.drop('quality', axis=1)
pca = PCA(n_components=4)
pca.fit(newdata)

print(f'coordinates of second vector: {pca.components_[1]}')
print('')
percentage = pca.explained_variance_ratio_[1] * 100
print(f'percentage captured by second principle component: {percentage}%')
