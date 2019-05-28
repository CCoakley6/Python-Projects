import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

train = pd.read_csv("/Users/Collin/Downloads/Refactored_Py_DS_ML_Bootcamp-master/13-Logistic-Regression/titanic_train.csv")
train.head()
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train, hue='Sex')
sns.countplot(x='Survived',data=train, hue='Pclass')
sns.distplot(train['Age'].dropna(),kde=False,bins=30)
train['Age'].plot.hist(bins=35)
train.info()
sns.countplot(x='SibSp',data=train)
train['Fare'].plot.hist(bins=40, figsize=(10,4))
sns.heatmap(train.isnull())
plt.figure(figsize=(10,7))
sns.boxplot(x='Pclass',y='Age',data=train)
def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):

        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age
train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)
sns.heatmap(train.isnull())
train.drop('Cabin',axis=1,inplace=True)
train.head()
sns.heatmap(train.isnull())
train.dropna(inplace=True)
sns.heatmap(train.isnull(),cmap='viridis')
##set dummy variables using Pandas
sex = pd.get_dummies(train['Sex'],drop_first=True)
sex.head()
embark = pd.get_dummies(train['Embarked'],drop_first = True)
embark.head()
train.head()
train.drop(['Embarked','Sex','Ticket','Name'], axis = 1, inplace=True)
train.columns
train = pd.concat([train,sex,embark], axis=1)
train.head()
train.drop('PassengerId', axis=1, inplace = True)
train.head()
X = train.drop('Survived', axis = 1)
y = train['Survived']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report

print (classification_report(y_test,predictions))
from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, predictions)
