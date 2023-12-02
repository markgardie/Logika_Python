from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton
 
class MainScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генератор чисeл")
        self.resize(800, 600)

        self.createWidgets()
        self.createLayouts()
        self.setupScreen()

    def createWidgets(self):
        pass

    def createLayouts(self):
        pass

    def setupScreen(self):

        self.row1.addWidget(self.questionLabel)

        self.row2.addWidget(self.ansRadio1)
        self.row2.addWidget(self.ansRadio2)

        self.row3.addWidget(self.ansRadio3)
        self.row3.addWidget(self.ansRadio4)

        self.mainColumn.addLayout(self.row1)
        self.mainColumn.addLayout(self.row2)
        self.mainColumn.addLayout(self.row3)

        self.setLayout(self.mainColumn)