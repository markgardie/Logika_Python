from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint 


class ScreenManager():

    def __init__(self):
        self.mainScreen = MainScreen()

        self.mainScreen.show()

        self.setListeners()

    def setListeners(self):
        self.mainScreen.generateButton.clicked.connect(self.generateNumber)

    def generateNumber(self):
        num = randint(1, 100)
        self.mainScreen.numberLabel.setText(str(num))
        self.mainScreen.infoLabel.setText("Переможець:")

class MainScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генератор чисeл")
        self.resize(800, 600)

        self.createWidgets()
        self.createLayouts()
        self.setupScreen()

    def createWidgets(self):
        self.generateButton = QPushButton("Згенерувати")
        self.numberLabel = QLabel("?")
        self.infoLabel = QLabel("Натисни на кнопку")

    def createLayouts(self):
        self.mainColumn = QVBoxLayout()

    def setupScreen(self):
        self.mainColumn.addWidget(self.infoLabel, alignment = Qt.AlignCenter)
        self.mainColumn.addWidget(self.numberLabel, alignment = Qt.AlignCenter)
        self.mainColumn.addWidget(self.generateButton, alignment = Qt.AlignCenter)
        
        self.setLayout(self.mainColumn)

app = QApplication([])
scr = ScreenManager()

app.exec_()