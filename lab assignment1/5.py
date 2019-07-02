import pandas as pd
import numpy as np
import random as rnd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC, LinearSVC
import warnings
warnings.filterwarnings("ignore")
from sklearn import metrics
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
train_data = pd.read_csv('./iris.csv')
print(train_data.info())
print(train_data['class'].value_counts())
data = train_data.select_dtypes(include=[np.number]).interpolate().dropna()
sns.FacetGrid(train_data,hue='class',size=5) \
.map(plt.scatter,"sepal length","sepal width") \
.add_legend()
sns.FacetGrid(train_data,hue='class',size=5) \
.map(plt.scatter,"petal length","petal width")\
.add_legend()
plt.show()
sns.pairplot(train_data,hue='class')
plt.show()

from sklearn.model_selection import train_test_split
train,test=train_test_split(train_data,test_size=0.4, random_state=0)
#print(train.shape)
#print(test.shape)
le = LabelEncoder()
numeric_features = train_data.select_dtypes(include=[np.number])
train_data["class"] = le.fit_transform(train_data["class"])
print(train_data.info())
train_X=train.drop("class", axis=1)
train_Y=train["class"]
test_X=test.drop("class", axis=1)
test_Y=test["class"]
numeric_features = data.select_dtypes(include=[np.number])

corr = numeric_features.corr()
print(corr)
data = data.drop("sepal width",axis=1)

from sklearn import metrics

#naive bayes model
model = GaussianNB()
model.fit(train_X, train_Y)
print(" naive Accuracy is : ", model.score(test_X,test_Y))

#knn
model = KNeighborsClassifier(n_neighbors=3)
model.fit(train_X, train_Y)
pred_Y = model.predict(test_X)
print(" knn Accuracy is : ",model.score(test_X,test_Y))


#svm
model = SVC()
model.fit(train_X, train_Y)
print(" svm Accuracy is : ",model.score(test_X,test_Y))
