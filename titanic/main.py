import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv(r"titanic\titanic.csv")

df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])

df['Embarked'].fillna("S", axis = 1)

df.drop(["Embarked"], axis = 1)

def fill_gender(gender):
    if gender == "male":
        return 1
    return 0

df["Sex"] = df.apply(fill_gender)

age1 = df[df["Pclass" == 1]]["Age"].median()
# age2
# age3

def fill_age(row):
    if pd.isnull(row["Age"]):
        if row["Pclass"] == 1:
            return age1
        # Pclass == 2 
        # Pclass == 3
    return row["Age"]

df["Age"] = df.apply(fill_age)


y = df["Survived"]
X = df.drop(["PassengerId", "Name", "Ticket", "Fare", "Cabin"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

classifier = KNeighborsClassifier()

classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred) * 100
print("Accuracy:", accuracy)
