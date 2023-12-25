from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TITLE = "Генератор чисeл"

class Screen(QWidget):

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
        pass

    def setupScreen(self):
        pass