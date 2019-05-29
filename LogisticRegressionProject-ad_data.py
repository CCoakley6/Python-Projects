##Project goal: predict whether a user clicked on an ad based on advertising data csv

##import Libraries
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

##convert data to dataframe
ad_data = pd.read_csv('/Users/Collin/Downloads/Refactored_Py_DS_ML_Bootcamp-master/13-Logistic-Regression/advertising.csv')
ad_data.head()


##explore the data visually
plt.figure(figsize=(10,7))
sns.distplot(ad_data['Age'],kde = False)
sns.jointplot(x = 'Area Income', y = 'Age', data = ad_data)

sns.jointplot(x = 'Daily Time Spent on Site', y = 'Age', data = ad_data)

sns.pairplot(ad_data, hue = 'Clicked on Ad')
plt.figure(figsize = (10,10))
sns.heatmap(ad_data.isnull(), cmap = 'viridis')

#LogisticRegression
from sklearn.model_selection import train_test_split

X = ad_data.drop('Clicked on Ad', axis = 1)

y = ad_data['Clicked on Ad']

##clean data
####drop data that isn't usable

X.head()
X.drop(['Ad Topic Line', 'City', 'Country', 'Timestamp'], axis = 1, inplace = True)
X.head()


y.head()

####test data to get predictions

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4)




from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

predictions = logmodel.predict(X_test)

####review data quality

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test, predictions))

print (confusion_matrix(y_test,predictions))
