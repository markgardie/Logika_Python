from utils.Constants import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QPushButton,
    QSpinBox,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QWidget
)

class BaseScreen(QWidget):

    def __init__(self, width, height, title):
        super().__init__()

        self.resize(width, height)
        self.setWindowTitle(title)
    
    def createWidgets(self):

        self.menuButton = QPushButton(MENU_BUTTON_TEXT)
        self.restButton = QPushButton(REST_BUTTON_TEXT)
        self.restSpinBox = QSpinBox()
        self.restSpinBox.setValue(START_MINUTES)
        self.minutesLabel = QLabel(MINUTES_TEXT)

        self.questionLabel = QLabel()

        self.answerButton = QPushButton()

    def createLayouts(self):
    
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()
        self.row4 = QHBoxLayout()

        self.mainColumn = QVBoxLayout()

    def setMainLayout(self):
        self.row1.addWidget(self.menuButton)
        self.row1.addStretch(1)
        self.row1.addWidget(self.restButton)
        self.row1.addWidget(self.restSpinBox)
        self.row1.addWidget(self.minutesLabel)

        self.row2.addWidget(self.questionLabel, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

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