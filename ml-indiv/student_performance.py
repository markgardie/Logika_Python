import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Кореляції

df = pd.read_csv('StudentPerformanceFactors.csv')

df_numeric = df.select_dtypes(include=['number'])
corr_matrix = df_numeric.corr()[['Exam Score']]

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=1, vmax=1)
plt.title("Correlation")
plt.show()

# Навчання моделі

# X, y
# train test split

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)
accuracy_r2 = r2_score(y_test, y_pred)

print(accuracy_r2)