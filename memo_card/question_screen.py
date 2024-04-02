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
        self.menuButton = QPushButton('Меню')
        self.restButton = QPushButton('Відпочити')
        self.nextButton = QPushButton('Відповісти')

        self.ansButton1 = QRadioButton("1")
        self.ansButton2 = QRadioButton("2")
        self.ansButton3 = QRadioButton("3")
        self.ansButton4 = QRadioButton("4")

        self.radioGroup = QButtonGroup()
        self.radioGroup.addButton(self.ansButton1)
        self.radioGroup.addButton(self.ansButton2)
        self.radioGroup.addButton(self.ansButton3)
        self.radioGroup.addButton(self.ansButton4)

        self.questionLabel = QLabel('Запитання')
        self.restLabel = QLabel('хвилин')
        self.resultLabel = QLabel('Правильно')
        self.rightAnswerLabel = QLabel('відповідь')

        self.restSpinBox = QSpinBox()

        self.questionGroupBox = QGroupBox('Варіанти відповідей')
        self.resultGroupBox = QGroupBox('Результат')


    def createLayouts(self):
        
        self.radioColumn1 = QVBoxLayout()
        self.radioColumn2 = QVBoxLayout()

        self.radioRow = QHBoxLayout()

        self.resultColumn = QVBoxLayout()

        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()
        self.row4 = QHBoxLayout()

        self.mainColumn = QVBoxLayout()


    def setupScreen(self):

        # ряд 1
        self.row1.addWidget(self.menuButton)
        self.row1.addStretch(1)
        self.row1.addWidget(self.restButton)
        self.row1.addWidget(self.restSpinBox)
        self.row1.addWidget(self.restLabel)

        # ряд 2
        self.row2.addWidget(self.questionLabel, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))


        # questionGroupBox
        self.radioColumn1.addWidget(self.ansButton1)
        self.radioColumn1.addWidget(self.ansButton2)
        self.radioColumn2.addWidget(self.ansButton3)
        self.radioColumn2.addWidget(self.ansButton4)

        self.radioRow.addLayout(self.radioColumn1)
        self.radioRow.addLayout(self.radioColumn2)

        self.questionGroupBox.setLayout(self.radioRow)

        # resultGroupBox
        self.resultColumn.addWidget(self.resultLabel)
        self.resultColumn.addWidget(self.rightAnswerLabel)

        self.resultGroupBox.setLayout(self.resultColumn)

        # ряд 3
        self.row3.addWidget(self.questionGroupBox)
        self.row3.addWidget(self.resultGroupBox)
        self.resultGroupBox.hide()

        # ряд 4
        self.row4.addStretch(1)
        self.row4.addWidget(self.nextButton, stretch=2)
        self.row4.addStretch(1)

        # головна колонка
        self.mainColumn.addLayout(self.row1, stretch=1)
        self.mainColumn.addLayout(self.row2, stretch=2)
        self.mainColumn.addLayout(self.row3, stretch=8)
        self.mainColumn.addLayout(self.row4)
        self.mainColumn.setSpacing(5)
        self.setLayout(self.mainColumn)