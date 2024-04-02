from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QHBoxLayout, QVBoxLayout, 
    QLabel, QRadioButton, QSpinBox, QGroupBox, QButtonGroup, QLineEdit
)

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
TITLE = "Memory card"


class EditScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.createWidgets()
        self.createLayouts()
        self.setupScreen()

    def createWidgets(self):
        self.questionLabel = QLabel('Введіть запитання:')
        self.rightLabel = QLabel('Введіть вірну відповідь:')
        self.wrongLabel1 = QLabel('Введіть першу хибну відповідь')
        self.wrongLabel2 = QLabel('Введіть другу хибну відповідь')
        self.wrongLabel3 = QLabel('Введіть третю хибну відповідь')

        self.questionEdit = QLineEdit()
        self.rightEdit = QLineEdit()
        self.wrongEdit1 = QLineEdit()
        self.wrongEdit2 = QLineEdit()
        self.wrongEdit3 = QLineEdit()

        self.headerStatLabel = QLabel('Статистика')
        self.headerStatLabel.setStyleSheet('font-size: 19px; font-weight: bold;')

        self.statsLabel = QLabel()

        self.backButton = QPushButton('Назад')
        self.addQuestionButton = QPushButton('Додати запитання')
        self.clearButton = QPushButton('Очистити')


    def createLayouts(self):
        
        self.labelsColumn = QVBoxLayout()
        self.editsColumn = QVBoxLayout()

        self.questionRow = QHBoxLayout()
        self.buttonsRow = QHBoxLayout()

        self.mainColumn = QVBoxLayout()

    def setupScreen(self):

        self.labelsColumn.addWidget(self.questionLabel)
        self.labelsColumn.addWidget(self.rightLabel)
        self.labelsColumn.addWidget(self.wrongLabel1)
        self.labelsColumn.addWidget(self.wrongLabel2)
        self.labelsColumn.addWidget(self.wrongLabel3)

        self.editsColumn.addWidget(self.questionEdit)
        self.editsColumn.addWidget(self.rightEdit)
        self.editsColumn.addWidget(self.wrongEdit1)
        self.editsColumn.addWidget(self.wrongEdit2)
        self.editsColumn.addWidget(self.wrongEdit3)

        self.questionRow.addLayout(self.labelsColumn)
        self.questionRow.addLayout(self.editsColumn)

        self.buttonsRow.addWidget(self.addQuestionButton)
        self.buttonsRow.addWidget(self.clearButton)

        self.mainColumn.addLayout(self.questionRow)
        self.mainColumn.addLayout(self.buttonsRow)
        self.mainColumn.addWidget(self.headerStatLabel)
        self.mainColumn.addWidget(self.statsLabel)
        self.mainColumn.addWidget(self.backButton)

        self.setLayout(self.mainColumn)