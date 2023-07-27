from ui.BaseScreen import BaseScreen
from utils.Constants import*
from PyQt5.QtWidgets import (
    QGroupBox,
    QRadioButton,
    QHBoxLayout,
    QVBoxLayout
)
from data.CardRepository import CardRepository
from random import randint

class QuestionScreen(BaseScreen):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.repository = CardRepository()
        self.randomCard = self.repository.cardsList[0]

        self.createWidgets()
        self.createLayouts()
        self.setGroupBox()
        self.setMainLayout()

    
    def createWidgets(self):
        super().createWidgets()

        self.questionLabel.setText(self.randomCard.question)

        self.questionGroupBox = QGroupBox(QUESTION_GROUP_BOX_TEXT)

        self.ansRadioButton1 = QRadioButton(self.randomCard.rightAnswer)
        self.ansRadioButton2 = QRadioButton(self.randomCard.wrongAnswer1)
        self.ansRadioButton3 = QRadioButton(self.randomCard.wrongAnswer2)
        self.ansRadioButton4 = QRadioButton(self.randomCard.wrongAnswer3)

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
