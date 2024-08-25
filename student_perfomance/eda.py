import pandas as pd
import numpy as nb
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('')

# Теплова мапа кореляції
plt.figure(figsize=(12, 6))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="Purples")

# Кругова діаграма
age_sorted = df["Age"].value_counts().sort_index()
plt.pie(age_sorted, labels = age_sorted.index, autopct='%.0f%%')
plt.title("Age Distribution")
plt.show()

# Стовпчата діаграма
plt.figure(figsize=(12,6))
sns.countplot(data=df,x='GradeClass',color="#b285bc")
plt.ylabel('Frequency')
plt.show()

# Лінійний графік
plt.figure(figsize=(12,6))
sns.lineplot(data=df,y='StudyTimeWeekly',x='GradeClass')