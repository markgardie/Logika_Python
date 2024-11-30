import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv(r"titanic\titanic.csv")

def fill_gender(gender):
    if gender == "male":
        return 1
    return 0 

df["Sex"] = df.apply(fill_gender)

age_1 = df[df["Pclass" == 1]]["Age"].median()
# age_2
# age_3

def fill_age(row):
    if pd.isnull(row["Age"]):
        if row["Pclass"] == 1:
            return age_1
        # pclass2
        # pclass3 
    return row["Age"]

df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])
df['Embarked'].fillna("S", axis = 1)
df.drop(["Embarked"], axis = 1)

     
