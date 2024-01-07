from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TITLE = "Генератор чисeл"

class MainScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.createWidgets()
        self.createLayouts()
        self.setupScreen()

    def createWidgets(self):
        self.infoLabel = QLabel("Натисни, аби дізнатись переможця")
        self.numberLabel = QLabel("?")

        self.generateButton = QPushButton("Згенерувати")

    def createLayouts(self):
        self.mainColumn = QVBoxLayout()

    def setupScreen(self):
        self.mainColumn.addWidget(self.infoLabel, alignment=Qt.AlignCenter)
        self.mainColumn.addWidget(self.numberLabel, alignment=Qt.AlignCenter)
        self.mainColumn.addWidget(self.generateButton, alignment=Qt.AlignCenter)

        self.setLayout(self.mainColumn)

