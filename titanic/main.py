# Крок 2. Створення моделі
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

y = df["Survived"]
X = df.drop(["PassengerId", "Name", "Ticket", "Fare", "Cabin"], axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

