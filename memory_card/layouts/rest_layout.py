from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QVBoxLayout,
       QGroupBox, QLabel)


#create widgets
restGroupBox = QGroupBox("Відпочинок")
timerLabel = QLabel("30")

#create layout
timerColumn = QVBoxLayout()

#add widgets, layouts
timerColumn.addWidget(timerLabel, alignment=Qt.AlignHCenter, stretch=2)
restGroupBox.setLayout(timerColumn)

restGroupBox.hide()