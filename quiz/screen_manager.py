from main_screen import MainScreen
from PyQt5.QtWidgets import QMessageBox

class ScreenManager():

    def __init__(self):

        self.mainScreen = MainScreen()
        self.messageScreen = QMessageBox()

        self.mainScreen.show()

        self.clickListeners()

    def clickListeners(self):
        self.mainScreen.ansRadio1.clicked.connect(self.win)
        self.mainScreen.ansRadio2.clicked.connect(self.lose)
        self.mainScreen.ansRadio3.clicked.connect(self.lose)
        self.mainScreen.ansRadio4.clicked.connect(self.lose)

    def win(self):
        self.messageScreen.setText("Перемога")
        self.messageScreen.exec_()
    
    
        