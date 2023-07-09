from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from Window import Window
from Constants import*

class QuizApp(QApplication):

    def __init__(self):
        super().__init__([])
        self.createWidgets()
        self.createLayout()
        self.setListeners()

    def createWidgets(self):
        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, TITLE)

        self.questionLabel = QLabel(QUESTION_TEXT)

        self.ansRadioButton1 = QRadioButton(ANS_1)
        self.ansRadioButton2 = QRadioButton(ANS_2)
        self.ansRadioButton3 = QRadioButton(ANS_3)
        self.ansRadioButton4 = QRadioButton(ANS_4)

    def createLayout(self):
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        mainColumn = QVBoxLayout()

        row1.addWidget(self.questionLabel, alignment=Qt.AlignCenter)

        row2.addWidget(self.ansRadioButton1, alignment=Qt.AlignCenter)
        row2.addWidget(self.ansRadioButton2, alignment=Qt.AlignCenter)

        row3.addWidget(self.ansRadioButton3, alignment=Qt.AlignCenter)
        row3.addWidget(self.ansRadioButton4, alignment=Qt.AlignCenter)

        mainColumn.addLayout(row1)
        mainColumn.addLayout(row2)
        mainColumn.addLayout(row3)

        self.window.setLayout(mainColumn)

    def setListeners(self):
        self.ansRadioButton1.clicked.connect(self.showLose)
        self.ansRadioButton2.clicked.connect(self.showLose)
        self.ansRadioButton3.clicked.connect(self.showWin)
        self.ansRadioButton4.clicked.connect(self.showLose)

    def showLose(self):
        message = QMessageBox()
        message.setText(LOSE_TEXT)
        message.exec_()

    def showWin(self):
        message = QMessageBox()
        message.setText(WIN_TEXT)
        message.exec_()         

