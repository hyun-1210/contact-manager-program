import pandas as pd
import seaborn
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

titanic_dataset=pd.read_csv('train.csv')

age_mean=titanic_dataset['Age'].mean()

titanic_dataset['Age'].fillna(age_mean, inplace=True)

titanic_dataset['Sex']=titanic_dataset['Sex'].map({'male':0, 'female':1})


titanic_dataset['FamilySize']=titanic_dataset['SibSp'] + titanic_dataset['Parch']

titanic_dataset['Title']=titanic_dataset['Name'].str.extract(r'([A-Za-z]+)\.')
title_mapping = {"Mr": 0, "Miss": 1, "Mrs": 2, "Master": 3} 
titanic_dataset['Title'] = titanic_dataset['Title'].map(title_mapping)


titanic_dataset['Age_group']=pd.cut(titanic_dataset['Age'], bins=[0, 10, 20, 60, 100], labels=[0, 1, 2, 3])


most_embarked=titanic_dataset['Embarked'].value_counts().idxmax()
titanic_dataset['Embarked'].fillna(most_embarked, inplace=True)
titanic_dataset['Embarked']=titanic_dataset['Embarked'].map({'S':0,'C':1, 'Q':2 })

features = ['Pclass', 'Sex', 'Age_group', 'FamilySize', 'Embarked', 'Title']
X =titanic_dataset[features]
y= titanic_dataset['Survived']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model= RandomForestClassifier(n_estimators=150, random_state=100)

model.fit(X_train, y_train)

predictions=model.predict(X_test)

accuracy= accuracy_score(y_test, predictions)

print(accuracy)


