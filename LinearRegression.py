import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/Collin/Downloads/Refactored_Py_DS_ML_Bootcamp-master/11-Linear-Regression/USA_Housing.csv')

df
df.columns
df
sns.distplot(df['Price'])
sns.heatmap(df.corr())
sns.heatmap(df.corr())
import sklearn
from sklearn.model_selection import train_test_split
y = df['Price']
df.columns
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state = 101)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.intercept_)
lm.coef_
cdf = pd.DataFrame(lm.coef_,X.columns,columns=['Coeff'])
cdf
from sklearn.datasets import load_boston
boston = load_boston()
boston.keys()
print(boston['DESCR'])

print(boston['target'])
#Predictions

cdf
predictions = lm.predict(X_test)
predictions
y_test
plt.scatter(y_test,predictions)
plt.hist(y_test-predictions,bins=30)
sns.distplot((y_test-predictions))
from sklearn import metrics
metrics.mean_absolute_error(y_test,predictions)
metrics.mean_squared_error(y_test, predictions)
