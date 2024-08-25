import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df= pd.read_csv("student_perfomance\Student_performance_data _.csv")

y = df["GPA"]
X = df.drop("GPA", axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lr = LinearRegression()
model = lr.fit(X_train, y_train)

model.score(X_test, y_test)