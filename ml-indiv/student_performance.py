import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('StudentPerformanceFactors.csv')

df_numeric = df.select_dtypes(include=['number'])
corr_matrix = df_numeric.corr()[['Exam Score']]

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=1, vmax=1)
plt.title("Correlation")
plt.show()