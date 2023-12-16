from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QHBoxLayout, QVBoxLayout, 
    QLabel, QRadioButton, QSpinBox, QGroupBox, QButtonGroup, QLineEdit
)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TITLE = "Memory card"


class QuestionScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.createWidgets()
        self.createLayouts()
        self.setupScreen()

    def createWidgets(self):
        self.questionEdit = QLineEdit()
        self.rightAnswerEdit = QLineEdit()
        self.wrongAnswerEdit1 = QLineEdit()
        self.wrongAnswerEdit2 = QLineEdit()
        self.wrongAnswerEdit3 = QLineEdit()


    def createLayouts(self):
        
        

        


    def setupScreen(self):

       