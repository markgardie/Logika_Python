from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QHBoxLayout, QVBoxLayout,
       QGroupBox, QButtonGroup, QRadioButton, 
       QPushButton, QLabel, QSpinBox)
from constants import*


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


