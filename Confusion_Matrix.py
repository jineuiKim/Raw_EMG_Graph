import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics

y_test = [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0] # 실제 클래스
y_pred = [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0] # 예측된 클래스

#confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
confusion_matrix = metrics.confusion_matrix(y_test, y_pred, normalize='true') #정규화환 결과
print(confusion_matrix)

accuracy = metrics.accuracy_score(y_test, y_pred)
print("정확도:", accuracy)

precision = metrics.precision_score(y_test, y_pred)
print("정밀도:", precision)

recall = metrics.recall_score(y_test, y_pred)
print("재현율:", recall)

f1 = metrics.f1_score(y_test, y_pred)
print("f1 점수:", f1)

sns.heatmap(confusion_matrix, annot=True, cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()