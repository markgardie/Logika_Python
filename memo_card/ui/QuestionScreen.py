from ui.BaseScreen import BaseScreen
from utils.Constants import*
from PyQt5.QtWidgets import (
    QGroupBox,
    QRadioButton,
    QHBoxLayout,
    QVBoxLayout
)
from random import randint


class QuestionScreen(BaseScreen):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.createWidgets()
        self.createLayouts()
        self.setGroupBox()
        self.setMainLayout()

    def createWidgets(self):
        super().createWidgets()

        self.questionLabel.setText(START_QUESTION)

        self.questionGroupBox = QGroupBox(QUESTION_GROUP_BOX_TEXT)

        self.ansRadioButton1 = QRadioButton(START_ANS1)
        self.ansRadioButton2 = QRadioButton(START_ANS2)
        self.ansRadioButton3 = QRadioButton(START_ANS3)
        self.ansRadioButton4 = QRadioButton(START_ANS4)

        self.answerButton.setText(ANSWER_BUTTON_TEXT)

    def createLayouts(self):
        super().createLayouts()

        self.cardColumn1 = QVBoxLayout()
        self.cardColumn2 = QVBoxLayout()
        self.cardMainRow = QHBoxLayout()
    
    def setGroupBox(self):

        self.cardColumn1.addWidget(self.ansRadioButton1)
        self.cardColumn1.addWidget(self.ansRadioButton2)
        self.cardColumn2.addWidget(self.ansRadioButton3)
        self.cardColumn2.addWidget(self.ansRadioButton4)

        self.cardMainRow.addLayout(self.cardColumn1)
        self.cardMainRow.addLayout(self.cardColumn2)

        self.questionGroupBox.setLayout(self.cardMainRow)

    def setMainLayout(self):
        super().setMainLayout()

        self.row3.addWidget(self.questionGroupBox)