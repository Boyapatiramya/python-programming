import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
model = SVC()
# there is other distribution for multinomial classes like Bernoulli Naive Bayes, Refer link
# Train the model using the training sets and check score
X_train = pd.read_csv('./glass.csv')
train_df, test_df = train_test_split(X_train, test_size=0.4, random_state=0)
X_train = train_df.drop("Type",axis=1)
Y_train = train_df["Type"]
X_test = test_df.drop("Type",axis=1)
Y_test = test_df["Type"]
combine = [train_df, test_df]
model = SVC(kernel='rbf')
model.fit(X_train, Y_train)
#Predict Output
predicted= model.predict(X_test)
print("train dataset",X_train)
print("test dataset",X_test)
print("prediction",predicted)
acc_nb = round(model.score(X_train, Y_train) * 100, 2)
print("rbf :",acc_nb)
# X_train.info()
# print('_'*40)
# print("y_train",Y_train)

