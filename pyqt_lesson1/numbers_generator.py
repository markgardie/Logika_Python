from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
 
app = QApplication([])
 
# головне вікно:
window = QWidget()
window.setWindowTitle('Визначити переможця')
window.move(100, 100)
window.resize(400, 200)
 
#віджети вікна: кнопка та надпис
button = QPushButton('Згенерувати')
text = QLabel('Натисни, аби дізнатися переможця')
winner = QLabel('?')
 
#положення віджетів
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
window.setLayout(line)
 
#функція, яка генерує і показує число
def show_winner():
    number = randint(1, 100)
    winner.setText(str(number))
    text.setText('Переможець:')
 
#обробка натискання на кнопку
button.clicked.connect(show_winner)
 
window.show()
app.exec_()
