import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv(r"titanic\titanic.csv")

df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])

df['Embarked'].fillna("S", axis = 1)

df.drop(["Embarked"], axis = 1)

