import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# Завантажуємо дані про абітурієнтів
data = pd.read_csv('applicant_data.csv')

y = data["admitted"]
X = data[["math_score", "eng_score", "ukr_score", "has_benefits"]]

