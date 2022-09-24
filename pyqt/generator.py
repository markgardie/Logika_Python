from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
window = QWidget()

window.move(0, 0)
window.resize(800, 600)

winner = QLabel("Натисни, щоби дізнатися переможця")
number = QLabel("?")
button = QPushButton("Згенерувати")

line = QVBoxLayout()
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(number, alignment = Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)

window.setLayout(line)

def findWinner():
    num = randint(1, 100)
    number.setText(str(num))
    winner.setText("Переможець")

button.clicked.connect(findWinner)

app.exec_()
window.show()