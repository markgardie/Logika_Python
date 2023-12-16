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
        self.answerGroupBox = QGroupBox('Результат')


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
