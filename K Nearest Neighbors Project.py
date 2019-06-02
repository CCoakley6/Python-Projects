import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from os import chdir
chdir('/Users/Collin/Documents/Refactored_Py_DS_ML_Bootcamp-master/14-K-Nearest-Neighbors')

df = pd.read_csv('KNN_Project_Data', index_col=1)
df.head()
df.info
plt.figure(figsize=(10,10))
sns.pairplot(data = df,hue='TARGET CLASS')
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS',axis=1))
scaled_data = scaler.transform(df.drop('TARGET CLASS',axis=1))

scaled_data
df_scaled = pd.DataFrame(scaled_data,columns = df.columns[:-1])
df_scaled.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_scaled, df['TARGET CLASS'], test_size = 0.3)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
pred
from sklearn.metrics import classification_report,confusion_matrix

print (classification_report(y_test,pred))

error_rate = []

for i in range(1,500):
    knn = KNeighborsClassifier(n_neighbors= i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))
error_rate
plt.figure(figsize=(10,10)),plt.plot(range(1,500),error_rate,linestyle='--',marker='o',markerfacecolor='red')

np.min(error_rate)
print(error_rate.index(np.min(error_rate)))

knn_retest = KNeighborsClassifier(n_neighbors=266)
knn_retest.fit(X_train, y_train)
pred_retest = knn_retest.predict(X_test)
pred_retest
print (classification_report(y_test,pred_retest))
