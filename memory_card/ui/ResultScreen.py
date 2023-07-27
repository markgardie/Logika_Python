from ui.BaseScreen import BaseScreen
from utils.Constants import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QGroupBox,
    QLabel,
    QHBoxLayout,
    QVBoxLayout
)

class ResultScreen(BaseScreen):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.createWidgets()
        self.createLayouts()
        self.setGroupBox()
        self.setMainLayout()

    
    def createWidgets(self):
        super().createWidgets()

        self.resultGroupBox = QGroupBox(RESULT_GROUP_BOX_TEXT)
        self.resultLabel = QLabel()

        self.answerButton.setText(RESULT_BUTTON_TEXT)

    
    def createLayouts(self):
        super().createLayouts()

        self.resultRow = QHBoxLayout()
    
    def setGroupBox(self):

        self.resultRow.addWidget(self.resultLabel, alignment= Qt.AlignCenter)

        self.resultGroupBox.setLayout(self.resultRow)

    def setMainLayout(self):
        super().setMainLayout()

        self.row3.addWidget(self.resultGroupBox)

    def setResult(self, right):
        if (right): self.resultLabel.setText(RIGHT_ANSWER_TEXT)
        else: self.resultLabel.setText(WRONG_ANSWER_TEXT)

    def setQuestion(self, question):
        self.questionLabel.setText(question)