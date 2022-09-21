from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


#Створюємо додаток
app = QApplication([])

#Створюємо вікно
window = QWidget()
window.setWindowTitle("Генератор чисел")
window.resize(600, 400)
window.move(0, 0)

#Перший надпис, підсказка
winner = QLabel()
winner.setText("Натиснути, щоб дізнатися переможця")

#Другий надпис, цифра
number = QLabel()
number.setText("?")

#Кнопка
button = QPushButton("Згенерувати")

#Позиція, розташування
line = QVBoxLayout()

app.exec_()
window.show()