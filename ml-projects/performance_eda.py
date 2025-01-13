import pandas as pd
import numpy as nb
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('')


age = df["Age"].value_counts().sort_index()
plt.figure(figsize=(12,6))
plt.pie(age, labels=age.index, autopct="%.0f%%")   
plt.title("Age Distribution")
plt.show()


plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="GradeClass", color = "#b285bc")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(12,6))
sns.lineplot(data=df, y="StudyTimeWeekly", x="GradeClass")
