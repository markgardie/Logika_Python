from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, 
                             QSpinBox, QGroupBox, QRadioButton)


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TITLE = ""

class MainScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.createWidgets()
        self.createLayouts()  
        self.setupScreen()

    def createWidgets(self):
        # загальні віджети
        self.menuButton = QPushButton("Меню")
        self.restButton = QPushButton("Відпочити")
        self.okButton = QPushButton("Відповісти")

        self.minutsLabel = QLabel("хвилин")
        self.questionLabel = QLabel("")

        self.restSpinBox = QSpinBox()

        # віджети питання
        self.ansRadio1 = QRadioButton("")
        self.ansRadio2 = QRadioButton("")
        self.ansRadio3 = QRadioButton("")
        self.ansRadio4 = QRadioButton("")

        self.answerGroupBox = QGroupBox("Варіанти відповідей")

        # віджети результату
        self.resultLabel = QLabel("Неправильно")
        self.rightAnswerLabel = QLabel("")
        self.resultGroupBox = QGroupBox("Результати")

    def createLayouts(self):
        # лейаути відповідей
        self.ansColumn1 = QVBoxLayout()
        self.ansColumn2 = QVBoxLayout()

        self.ansRow = QHBoxLayout()

        # головні лейаути
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()
        self.row4 = QHBoxLayout()

        self.mainColumn = QVBoxLayout()

        # лейаути результату
        self.resultRow = QHBoxLayout()
        self.rightRow = QHBoxLayout()
        self.resultColumn = QVBoxLayout()

    def setupScreen(self):
        # налаштування answerGroupBox
        self.ansColumn1.addWidget(self.ansRadio1)
        self.ansColumn1.addWidget(self.ansRadio2)

        self.ansColumn2.addWidget(self.ansRadio3)
        self.ansColumn2.addWidget(self.ansRadio4)

        self.ansRow.addLayout(self.ansColumn1)
        self.ansRow.addLayout(self.ansColumn2)

        self.answerGroupBox.setLayout(self.ansRow)

        # налаштування resultGroupBox
        self.resultRow.addWidget(self.resultLabel)
        self.rightRow.addWidget(self.rightAnswerLabel, alignment=Qt.AlignCenter)
        self.resultColumn.addLayout(self.resultRow)
        self.resultColumn.addLayout(self.rightRow)
        self.resultGroupBox.setLayout(self.resultColumn)



