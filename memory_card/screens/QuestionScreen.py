from utils.BaseScreen import BaseScreen
from utils.Constants import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QPushButton,
    QSpinBox,
    QLabel,
    QGroupBox,
    QRadioButton,
    QHBoxLayout,
    QVBoxLayout
)

class QuestionScreen(BaseScreen):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        

        self.createWidgets()
        self.createLayouts()
        self.setGroupBox()
        self.setMainLayout()
        self.setupListeners()

    
    def createWidgets(self):

        self.menuButton = QPushButton(MENU_BUTTON_TEXT)
        self.restButton = QPushButton(REST_BUTTON_TEXT)
        self.restSpinBox = QSpinBox()
        self.restSpinBox.setValue(START_MINUTES)
        self.minutesLabel = QLabel(MINUTES_TEXT)

        self.questionLabel = QLabel(TEST_QUESTION)

        self.questionGroupBox = QGroupBox(QUESTION_GROUP_BOX_TEXT)

        self.ansRadioButton1 = QRadioButton(TEST_ANS1)
        self.ansRadioButton2 = QRadioButton(TEST_ANS2)
        self.ansRadioButton3 = QRadioButton(TEST_ANS3)
        self.ansRadioButton4 = QRadioButton(TEST_ANS4)

        self.answerButton = QPushButton(ANSWER_BUTTON_TEXT)

    def createLayouts(self):
        self.cardColumn1 = QVBoxLayout()
        self.cardColumn2 = QVBoxLayout()
        self.cardMainRow = QHBoxLayout()

        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()
        self.row4 = QHBoxLayout()

        self.mainColumn = QVBoxLayout()
    
    def setGroupBox(self):

        self.cardColumn1.addWidget(self.ansRadioButton1)
        self.cardColumn1.addWidget(self.ansRadioButton2)
        self.cardColumn2.addWidget(self.ansRadioButton3)
        self.cardColumn2.addWidget(self.ansRadioButton4)

        self.cardMainRow.addLayout(self.cardColumn1)
        self.cardMainRow.addLayout(self.cardColumn2)

        self.questionGroupBox.setLayout(self.cardMainRow)

    def setMainLayout(self):
        self.row1.addWidget(self.menuButton)
        self.row1.addStretch(1)
        self.row1.addWidget(self.restButton)
        self.row1.addWidget(self.restSpinBox)
        self.row1.addWidget(self.minutesLabel)

        self.row2.addWidget(self.questionLabel, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

        self.row3.addWidget(self.questionGroupBox)

        self.row4.addStretch(1)
        self.row4.addWidget(self.answerButton, stretch=2)
        self.row4.addStretch(1)

        self.mainColumn.addLayout(self.row1, stretch=1)
        self.mainColumn.addLayout(self.row2, stretch=2)
        self.mainColumn.addStretch(1)
        self.mainColumn.addLayout(self.row3, stretch=8)
        self.mainColumn.addStretch(1)
        self.mainColumn.addLayout(self.row4, stretch=1)

        self.setLayout(self.mainColumn)



    def setupListeners(self):
        pass