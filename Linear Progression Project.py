#Project: Linear Regression of eCommerce dataset to determine if mobile or web is more effective

#Import packages
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

%matplotlib inline

df = pd.read_csv('/Users/Collin/Downloads/Refactored_Py_DS_ML_Bootcamp-master/11-Linear-Regression/Ecommerce Customers')
df
df.columns
sns.jointplot('Time on Website', 'Yearly Amount Spent', data= df)
sns.jointplot('Time on App', 'Yearly Amount Spent', data= df)
sns.jointplot('Time on App', 'Length of Membership', df, 'hex',)
sns.pairplot(df)
lm = sns.lmplot('Length of Membership', 'Yearly Amount Spent', data=df)
from sklearn.model_selection import train_test_split
df.columns
y = df['Yearly Amount Spent']
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership', 'Yearly Amount Spent']]
X_train, X_test, y_train, y_test = train_test_split(X, y)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.intercept_)
lm.coef_
cdf = pd.DataFrame(lm.coef_,X.columns,columns = ['Coeff'])
cdf
#Predictions
predictions = lm.predict(X_test)
predictions
y_test
sns.scatterplot(y_test,predictions)
plt.pyplot.hist(y_test-predictions,bins=30)
sns.distplot((y_test-predictions))
from sklearn import metrics
metrics.mean_absolute_error(y_test,predictions,multioutput='uniform_average')
metrics.mean_squared_error(y_test, predictions)
 
