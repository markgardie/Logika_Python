import pandas as pd 


df = pd.read_csv(r"titanic\titanic.csv")
df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])
df['Embarked'].fillna("S", axis = 1)
df.drop(["Embarked"], axis = 1)

age_1 = df[df["Pclass" == 1]]["Age"].median()
age_2 = df[df["Pclass" == 2]]["Age"].median()
age_3 = df[df["Pclass" == 3]]["Age"].median()


def fill_age(row):
    if pd.isnull(row["Age"]):
        if row["Pclass"] == 1:
            return age_1
        if row["Pclass"] == 2:
            return age_2
        if row["Pclass"] == 3:
            return age_3
    return row["Age"]

df["Age"] = df.apply(fill_age)

def fill_gender(gender):
    if gender == "male":
        return 1
    return 0

df["Sex"] = df.apply(fill_gender)

# Крок 2. Створення моделі
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import confusion_matrix, accuracy_score

# y = df["Survived"]
# X = df.drop(["PassengerId", "Name", "Ticket", "Fare", "Cabin"], axis = 1)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# classifier = KNeighborsClassifier()

# classifier.fit(X_train, y_train)
# y_pred = classifier.predict(X_test)

# accuracy = accuracy_score(y_test, y_pred) * 100

# print("Точність:", accuracy)
