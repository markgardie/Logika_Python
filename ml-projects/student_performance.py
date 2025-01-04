import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Correlation
df = pd.read_csv('/')

df_numeric = df.select_dtypes(include=['number'])
corr = df_numeric.corr()[["Exam Score"]]

sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5, vmin=-1, vmax=1)
plt.title("Correlation")
plt.show()

# Regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# x, y
y = df["ExamScore"]
X = df.drop(["ExamScore", "Gender"])

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)
r2_accuracy = r2_score(y_test, y_pred)
print(r2_accuracy)

# Regression plot
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color="blue", alpha=0.5, label = "Predicted vs Actual")

