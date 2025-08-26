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

most_embarked=titanic_dataset['Embarked'].value_counts().idxmax()
titanic_dataset['Embarked'].fillna(most_embarked, inplace=True)
titanic_dataset['Embarked']=titanic_dataset['Embarked'].map({'S':0,'C':1, 'Q':2 })

features = ['Pclass', 'Sex', 'Age', 'FamilySize', 'Embarked']
X =titanic_dataset[features]
y= titanic_dataset['Survived']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model= RandomForestClassifier(n_estimators=100, random_state=100)

model.fit(X_train, y_train)

predictions=model.predict(X_test)

accuracy= accuracy_score(y_test, predictions)

print(accuracy)


