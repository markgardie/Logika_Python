from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QVBoxLayout,
       QGroupBox, QLabel)

#create widgets
resultGroupBox = QGroupBox("Результати")
resultLabel = QLabel("")
correctAnswerLabel = QLabel("")

#create layout
resultColumn = QVBoxLayout()

#add widgets, layouts
resultColumn.addWidget(resultLabel, alignment=(Qt.AlignLeft | Qt.AlignTop))
resultColumn.addWidget(correctAnswerLabel, alignment=Qt.AlignHCenter, stretch=2)
resultGroupBox.setLayout(resultColumn)
resultGroupBox.hide()