from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
TITLE = "Randomizer"
HINT_TEXT = "Натисни на кнопку, аби дізнатись переможця"
QUESTION_TEXT = "?"
WINNER_TEXT = "Переможець:"
GENERATE_TEXT = "Згенерувати"

class Window(QWidget):

    def __init__(self, width, height, title):
        super().__init__()

        self.setWindowTitle(title)
        self.resize(width, height)


class RandomizerApp(QApplication):

    def createWidgets(self):
        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, TITLE)

        self.hintLabel = QLabel(HINT_TEXT)
        self.numberLabel = QLabel(QUESTION_TEXT)

        self.generateButton = QPushButton(GENERATE_TEXT)

    def designLayout(self):
        column = QVBoxLayout()

        column.addWidget(self.hintLabel, alignment=Qt.AlignCenter)
        column.addWidget(self.numberLabel, alignment=Qt.AlignCenter)
        column.addWidget(self.generateButton, alignment=Qt.AlignCenter)

        self.window.setLayout(column)

    def listener(self):
        self.generateButton.clicked.connect(self.generateNumber)

    def generateNumber(self):
        number = randint(1, 100)
        self.numberLabel.setText(str(number))
        self.hintLabel.setText(WINNER_TEXT)


