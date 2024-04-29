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