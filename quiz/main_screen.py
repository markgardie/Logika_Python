from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TITLE = "Вікторина"

class MainScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.createWidgets()
        self.createLayouts()
        self.setupScreen()

    def createWidgets(self):
        self.questionLabel = QLabel("Питання?")
        self.ansRadio1 = QRadioButton("Відповідь 1")
        self.ansRadio2 = QRadioButton("Відповідь 2")
        self.ansRadio3 = QRadioButton("Відповідь 3")
        self.ansRadio4 = QRadioButton("Відповідь 4")

    def createLayouts(self):
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()

        self.mainColumn = QVBoxLayout()

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