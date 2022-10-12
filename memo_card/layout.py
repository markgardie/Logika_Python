from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QHBoxLayout, QVBoxLayout,
       QGroupBox, QButtonGroup, QRadioButton, 
       QPushButton, QLabel, QSpinBox)
from constants import*


#Створити вікно

#create widgets
menuButton = QPushButton("Меню")
timerButton = QPushButton("Відпочити")
answerButton = QPushButton("Відповісти")


ansRadioButton1 = QRadioButton(RIGHT_TEXT)
ansRadioButton2 = QRadioButton(WRONG_TEXT1)
ansRadioButton3 = QRadioButton(WRONG_TEXT2)
ansRadioButton4 = QRadioButton(WRONG_TEXT3)


timer = QSpinBox()
timer.setValue(30)

questionLabel = QLabel(QUESTION_TEXT)
minutesLabel = QLabel("хвилин")

ansButtonGroup = QButtonGroup()
ansGroupBox = QGroupBox("Варіанти відповідей")
resultGroupBox = QGroupBox("Результати") #Перенести layout результату в інший файл

#Додати кнопки до ButtonGroup


#create layout
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()

column1 = QVBoxLayout()
column2 = QVBoxLayout()
mainColumn = QVBoxLayout()

#add widget
column1.addWidget(ansRadioButton1, alignment=Qt.AlignCenter)
column1.addWidget(ansRadioButton2, alignment=Qt.AlignCenter)

column2.addWidget(ansRadioButton3, alignment=Qt.AlignCenter)
column2.addWidget(ansRadioButton4, alignment=Qt.AlignCenter)

row1.addWidget(menuButton, alignment=Qt.AlignCenter)
row1.addStretch(1)
row1.addWidget(timerButton, alignment=Qt.AlignCenter)
row1.addWidget(timer, alignment=Qt.AlignCenter)
row1.addWidget(minutesLabel, alignment=Qt.AlignCenter)

row2.addWidget(questionLabel, alignment=Qt.AlignCenter)

row3.addLayout(column1)
row3.addLayout(column2)
ansGroupBox.setLayout(row3)

row4.addStretch(1)
row4.addWidget(answerButton, alignment=Qt.AlignCenter)
row4.addStretch(1)

mainColumn.addLayout(row1)
mainColumn.addLayout(row2)
mainColumn.addLayout(row3)
mainColumn.addLayout(row4)
mainColumn.setSpacing(5)



