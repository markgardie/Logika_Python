import pandas as pd 

df = pd.read_csv(r'ml\titanic.csv')
print(df.info())

age_1 = df[df["Pclass"] == 1]["Age"].median()
age_2 = df[df["Pclass"] == 2]["Age"].median()
age_3 = df[df["Pclass"] == 3]["Age"].median()

def fill_age(row):
    if pd.isnull(row["Age"]):
        if row["Pclass"] == 1:
            return age_1
        if row["Pclass"] == 2:
            return age_2
        return age_3
    return row["Age"]

df["Age"] = df.apply(fill_age, axis=1)

def fill_sex(row):
    if row["Sex"] == "male":
        return 1
    return 0
   
df["Sex"] = df.apply(fill_sex, axis=1)

df["Embarked"].fillna("S", inplace=True)

df[list(pd.get_dummies(df["Embarked"].columns))] = pd.get_dummies(df["Embarked"])

df.drop(["PassengerId", "Name", "Ticket", "Cabin", "Embarked"], axis = 1, inplace=True)


# Крок 2. Створення моделі
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

