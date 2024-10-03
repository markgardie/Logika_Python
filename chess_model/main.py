import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Завантаження даних
df = pd.read_csv('chess_model\chess_games.csv')

# Підготовка даних
# Вибір ознак для моделі
features = ['turns', 'white_rating', 'black_rating', 'opening_moves', 'opening_shortname']
target = 'winner'

# Кодування категоріальних змінних
le = LabelEncoder()
df['opening_shortname'] = le.fit_transform(df['opening_shortname'])

# Підготовка X (ознаки) та y (цільова змінна)
X = df[features]
y = df[target]

# Розділення даних на навчальний та тестовий набори
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Масштабування ознак
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Створення та навчання моделі KNN
knn = KNeighborsClassifier(n_neighbors=5)  # Можна експериментувати з кількістю сусідів
knn.fit(X_train_scaled, y_train)

# Прогнозування на тестовому наборі
y_pred = knn.predict(X_test_scaled)

# Оцінка моделі
accuracy = accuracy_score(y_test, y_pred)
print(f"Точність моделі: {accuracy:.2f}")

# Визначення важливості ознак
feature_importance = pd.DataFrame({'feature': features, 
                                   'importance': np.mean(np.abs(X_train_scaled), axis=0)})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print("\nВажливість ознак:")
print(feature_importance)