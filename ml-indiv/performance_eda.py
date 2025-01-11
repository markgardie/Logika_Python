import pandas as pd
import numpy as nb
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('')

plt.figure(figsize=(12,6))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='Purples')

age = df["Age"].value_counts().sort_index()
plt.figure(figsize=(12,6))
plt.pie(age, labels = age.index, autopct='%.0f%%')
plt.title("Age Distribution")
plt.show()

gender = df['Gender'].value_counts().sort_index()
plt.figure(figsize=(12,6))
plt.pie(gender,labels=gender.index,autopct='%.0f%%',startangle=90)
plt.title('Gender Distribution')
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(data=df, x = "GradeClass", color = "#b285bc")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(data=df,x='Ethnicity',palette='ch:start=.2,rot=-.3')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x="GradeClass", y="StudyTimeWeekly")

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x="GradeClass", y="Absences")