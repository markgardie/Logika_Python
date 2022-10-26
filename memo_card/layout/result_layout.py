from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout,
       QGroupBox, QLabel)
from constants import*

#widgets
resultGroupBox = QGroupBox("Результати")
resultLabel = QLabel("")
correctAnswerLabel = QLabel(RIGHT_TEXT)

#lines
resultColumn = QVBoxLayout()

#add widgets
resultColumn.addWidget(resultLabel, alignment=(Qt.AlignLeft | Qt.AlignTop))
resultColumn.addWidget(correctAnswerLabel, alignment= Qt.AlignCenter)

resultGroupBox.setLayout(resultColumn)
resultGroupBox.hide()