from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QHBoxLayout, QVBoxLayout, 
    QLabel, QRadioButton, QSpinBox, QGroupBox, QButtonGroup
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
        self.назва_віджета = Назва_класу(текст)


    def createLayouts(self):
        
        self.назва_віджета = Назва_класу()

    def setupScreen(self):

        pass