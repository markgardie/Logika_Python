from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint


GENERATE_TEXT = "Згенерувати"
HINT_TEXT = "Натисни, аби дізнатись переможця"
WINNER_TEXT = "Переможець:"
QUESTION_TEXT = "?"


class RandomizerApp():

    def __init__(self):
            
        self.createWidgets()
        self.setMyLayout()
        self.listener()
        self.startApp()

    def createWidgets(self):
        self.app = QApplication([])

        self.window = QWidget()

        self.generateBtn = QPushButton(GENERATE_TEXT)

        self.hintLabel = QLabel(HINT_TEXT)
        self.numberLabel = QLabel(QUESTION_TEXT)

    
    def setMyLayout(self):

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

    def startApp(self):
        self.app.exec_
        self.window.show()


myApp = RandomizerApp()

