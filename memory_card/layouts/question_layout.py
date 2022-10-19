from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
       QGroupBox, QButtonGroup, QRadioButton, 
       QPushButton, QLabel, QSpinBox)
from constants import*
from layouts.result_layout import resultGroupBox

#create window
questionWindow = QWidget()
questionWindow.resize(CARD_WIDTH, CARD_HEIGHT)
questionWindow.move(WINDOW_X, WINDOW_Y)
questionWindow.setWindowTitle('Memory Card')


#create widgets
menuButton = QPushButton("Меню")
timerButton = QPushButton("Відпочити")
answerButton = QPushButton("Відповісти")

ansRadioButton1 = QRadioButton('')
ansRadioButton2 = QRadioButton('')
ansRadioButton3 = QRadioButton('')
ansRadioButton4 = QRadioButton('')


timer = QSpinBox()
timer.setValue(30)

questionLabel = QLabel(QUESTION_TEXT)
minutesLabel = QLabel("хвилин")

ansButtonGroup = QButtonGroup()
ansGroupBox = QGroupBox("Варіанти відповідей")

ansButtonGroup.addButton(ansRadioButton1)
ansButtonGroup.addButton(ansRadioButton2)
ansButtonGroup.addButton(ansRadioButton3)
ansButtonGroup.addButton(ansRadioButton4)


#create layout
row1 = QHBoxLayout()
row2 = QHBoxLayout()
ansGroupBoxRow = QHBoxLayout()
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

ansGroupBoxRow.addLayout(column1)
ansGroupBoxRow.addLayout(column2)
ansGroupBox.setLayout(ansGroupBoxRow)

row1.addWidget(menuButton, alignment=Qt.AlignCenter)
row1.addStretch(1)
row1.addWidget(timerButton, alignment=Qt.AlignCenter)
row1.addWidget(timer, alignment=Qt.AlignCenter)
row1.addWidget(minutesLabel, alignment=Qt.AlignCenter)

row2.addWidget(questionLabel, alignment=Qt.AlignCenter)

row3.addWidget(ansGroupBox)
row3.addWidget(resultGroupBox)

row4.addStretch(1)
row4.addWidget(answerButton, alignment=Qt.AlignCenter)
row4.addStretch(1)

mainColumn.addLayout(row1)
mainColumn.addLayout(row2)
mainColumn.addLayout(row3)
mainColumn.addLayout(row4)
mainColumn.setSpacing(5)

questionWindow.setLayout(mainColumn)
