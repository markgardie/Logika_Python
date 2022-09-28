from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout

app = QApplication([])
window = QWidget()

window.resize(800, 600)
window.move(0, 0)

question = QLabel("В якому році канал отримав «золоту кнопку» від YouTube?")

ans1 = QRadioButton("2005")
ans2 = QRadioButton("2010")
ans3 = QRadioButton("2015")
ans4 = QRadioButton("2020")

h_layout1 = QHBoxLayout()
h_layout2 = QHBoxLayout()
h_layout3 = QHBoxLayout()

v_layout = QVBoxLayout()

h_layout1.addWidget(question, alignment=Qt.AlignCenter)
h_layout2.addWidget(ans1, alignment=Qt.AlignCenter)
h_layout2.addWidget(ans2, alignment=Qt.AlignCenter)
h_layout3.addWidget(ans3, alignment=Qt.AlignCenter)
h_layout3.addWidget(ans4, alignment=Qt.AlignCenter)



app.exec_()
window.show()