import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

dataset = pd.read_csv("emgraw.csv")
x = pd.DataFrame(dataset.iloc[:,1:-1])
y = dataset.iloc[:,-1].values


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1, shuffle=True) #split the data into training and test sets
print(x_test)
print(x_train)
print(y_test)
print(y_train)
logmodel = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,intercept_scaling=1, max_iter=100, multi_class='auto', n_jobs=None,
                              penalty='l2', random_state=None, solver='saga', tol=0.0001, verbose=0, warm_start=False)

print(logmodel.fit(x_train, y_train))

y_pred = logmodel.predict(x_test)

print(y_pred)

confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
print(confusion_matrix)

#accuracy = metrics.accuracy_score(y_test, y_pred)
#print("정확도:", accuracy)

#precision = metrics.precision_score(y_test, y_pred)
#print("정밀도:", precision)

#recall = metrics.recall_score(y_test, y_pred)
#print("재현율:", recall)

#f1 = metrics.f1_score(y_test, y_pred)
#print("f1 점수:", f1)

sns.heatmap(confusion_matrix, annot=True, cmap='Blues',
            xticklabels=['hand at rest', 'fist', 'wrist flex', 'wrist ext', 'radial dev', 'ulnar dev', 'palm'],
            yticklabels=['hand at rest', 'fist', 'wrist flex', 'wrist ext','radial dev', 'ulnar dev', 'palm'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

