import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint


GENERATE_TEXT = "Згенерувати"
HINT_TEXT = "Натисни, аби дізнатись переможця"
WINNER_TEXT = "Переможець:"
QUESTION_TEXT = "?"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
TITLE = "Randomizer"


class Window(QWidget):

    def __init__(self, width, height, title):
        super().__init__()

        self.resize(width, height)
        self.setWindowTitle(title)

class RandomizerApp(QApplication):

    def __init__(self):
        super().__init__([])
            
        self.widgets()
        self.layout()
        self.listener()

    def widgets(self):
        self.app = QApplication([])

        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, TITLE)

        self.generateBtn = QPushButton(GENERATE_TEXT)

        self.hintLabel = QLabel(HINT_TEXT)
        self.numberLabel = QLabel(QUESTION_TEXT)

    
    def layout(self):

        column = QVBoxLayout()

        column.addWidget(self.hintLabel, alignment = Qt.AlignCenter)
        column.addWidget(self.numberLabel, alignment = Qt.AlignCenter)
        column.addWidget(self.generateBtn, alignment = Qt.AlignCenter)
        
        self.window.setLayout(column)

    def listener(self):
        self.generateBtn.clicked.connect(self.generateNumber)

    def generateNumber(self):
        
        self.hintLabel.setText(WINNER_TEXT)
        number = randint(1, 100)
        self.numberLabel.setText(str(number))



myApp = RandomizerApp()
myApp.window.show()
myApp.exec_()
