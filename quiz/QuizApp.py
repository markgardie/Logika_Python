
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox
from Window import Window
from Constants import *

class QuizApp(QApplication):

    def __init__(self):
        super().__init__([])
            
        self.widgets()
        self.layout()
        self.listener()


    def widgets(self):

        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, TITLE)

        self.questionLabel = QLabel(QUESTION_TEXT)

        self.ansRadioButton1 = QRadioButton(ANS_1)
        self.ansRadioButton2 = QRadioButton(ANS_2)
        self.ansRadioButton3 = QRadioButton(ANS_3)
        self.ansRadioButton4 = QRadioButton(ANS_4)

        self.message = QMessageBox()

    
    def layout(self):
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


    def listener(self):
        self.ansRadioButton1.clicked.connect(self.lose)
        self.ansRadioButton2.clicked.connect(self.lose)
        self.ansRadioButton3.clicked.connect(self.win)
        self.ansRadioButton4.clicked.connect(self.lose)

    
    def lose(self):
        self.message.setText(LOSE_TEXT)
        self.message.exec_()

    
    def win(self):
        self.message.setText(WIN_TEXT)
        self.message.exec_()


app = QuizApp()
app.window.show()
app.exec_()
