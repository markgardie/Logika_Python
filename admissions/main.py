import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# Завантажуємо дані про абітурієнтів
data = pd.read_csv('applicant_data.csv')

y = data["admitted"]
X = data[["math_score", "eng_score", "ukr_score", "has_benefits"]]

logreg = LogisticRegression()
scores = cross_val_score(logreg, X, y, scoring = "accuracy", cv = 5)
print(f"Accuracy: {scores.mean()*100:.2f}%")

logreg.fit(X.values, y)

predictions = []

for row in data.iterrows():
    math_score = row["math_score"]
    eng_score = row["eng_score"]
    ukr_score = row["ukr_score"]
    has_benefits = row["has_benefits"]
    
    rating_score = calculate_rating(math_score, eng_score, ukr_score)
    prediction = logreg.predict([math_score, eng_score, ukr_score])

    predictions.append(
        {
        'math_score': math_score,
        'eng_score': eng_score,
        'ukr_score': ukr_score,
        'has_benefits': has_benefits,
        'rating_score': rating_score,
        'prediction': prediction[0]
    }
    )

# Сортуємо абітурієнтів за рейтинговим балом
regular_applicants = [p for p in predictions if not p['has_benefits']]
special_applicants = [p for p in predictions if p['has_benefits']]

regular_applicants.sort(key=lambda x: x['rating_score'], reverse=True)
special_applicants.sort(key=lambda x: x['rating_score'], reverse=True)


