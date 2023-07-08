from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox
from Window import Window
from Constants import *

class QuizApp(QApplication):

    def widgets(self):

        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, TITLE)

        self.questionLabel = QLabel(QUESTION_TEXT)

        self.ansRadioButton1 = QRadioButton(ANS_1)
        self.ansRadioButton2 = QRadioButton(ANS_2)
        self.ansRadioButton3 = QRadioButton(ANS_3)
        self.ansRadioButton4 = QRadioButton(ANS_4)

    def layout(self):

        mainColumn = QVBoxLayout()

        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        row1.addWidget(self.questionLabel, alignment=Qt.ALignCenter)

        row2.addWidget(self.ansRadioButton1, alignment=Qt.ALignCenter)
        row2.addWidget(self.ansRadioButton2, alignment=Qt.ALignCenter)

        row3.addWidget(self.ansRadioButton3, alignment=Qt.ALignCenter)
        row3.addWidget(self.ansRadioButton4, alignment=Qt.ALignCenter)

        mainColumn.addLayout(row1)
        mainColumn.addLayout(row2)
        mainColumn.addLayout(row3)

        self.window.setLayout(mainColumn)


    