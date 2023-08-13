from ui.BaseScreen import BaseScreen
from utils.Constants import*
from PyQt5.QtWidgets import (
    QGroupBox,
    QRadioButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel
)
from random import randint


class ResultScreen(BaseScreen):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.createWidgets()
        self.createLayouts()
        self.setGroupBox()
        self.setMainLayout()

    def createWidgets(self):
        super().createWidgets()

        self.questionLabel.setText(START_QUESTION)

        self.resultGroupBox = QGroupBox(RESULT_GROUP_BOX_TEXT)
        self.resultLabel = QLabel()

        self.answerButton.setText(RESULT_BUTTON_TEXT)

    def createLayouts(self):
        super().createLayouts()

        self.resultRow = QHBoxLayout()
    
    def setGroupBox(self):

        self.resultRow.addWidget(self.resultLabel)
        self.resultGroupBox.setLayout(self.resultRow)

    def setMainLayout(self):
        super().setMainLayout()

        self.row3.addWidget(self.resultGroupBox)