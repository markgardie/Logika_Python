import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("GoogleApps.csv")

# --- ЧАСТИНА 2: Базові діаграми ---

# Діаграма 1: Гістограма розподілу рейтингів
plt.figure(figsize=(10, 6))
sns.histplot(df["Rating"], bins = 30, kde = True, color = "skyblue")
plt.title("Розподіл рейтингів")
plt.xlabel("Рейтинг")
plt.ylabel("Кількість")
plt.show()

# Діаграма 2: Топ-10 категорій (Стовпчикова діаграма)
plt.figure(figsize=(12, 6))
top10 = df["Category"].value_counts().head(10)
sns.barplot(x = top10.values, y = top10.index, palette="viridis")
plt.title("Топ 10 категорій")
plt.xlabel("Кількість")
plt.show()

# Діаграма 3: Безкоштовні vs Платні (Кругова діаграма)
plt.figure(figsize=(12, 6))
free_paid = df["Type"].value_counts()
plt.pie(free_paid, 
        labels=free_paid.index, 
        autopct="%1.1f%%", 
        startangle=140,
        colors = ['#66b3ff','#ff9999'])
plt.title("Безкоштовні vs Платні")
plt.show()

# --- ЧАСТИНА 3: Додаткові дослідження ---

# Дослідження А: Залежність рейтингу від вікового обмеження (Boxplot)
plt.figure(figsize=(12, 6))
sns.boxplot(x = "Content Rating", y = "Rating", data = df, palette="Set2")
plt.title("Рейтинг за віком")
plt.xticks(rotation = 45)
plt.show()

# Дослідження Б: Кореляційна матриця (Heatmap)
num_df = df[["Rating", "Size", "Installs", "Price"]]
corr = num_df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Кореляції")
plt.show()

