from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QVBoxLayout,
       QGroupBox, QLabel)

#widgets
timerGroupBox = QGroupBox("Відпочинок")
timerLabel = QLabel("")

#lines
timerColumn = QVBoxLayout()

#add widgets
timerColumn.addWidget(timerLabel, alignment= Qt.AlignCenter)

timerGroupBox.setLayout(timerColumn)
timerGroupBox.hide()