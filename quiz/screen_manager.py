from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from main_screen import MainScreen

class ScreenManager():

    def __init__(self):
        self.mainScreen = MainScreen()
        self.mainScreen.show()

        self.setListeners()

    def setListeners(self):
        self.mainScreen.ansRadio1.clicked.connect(self.showWin)
        self.mainScreen.ansRadio2.clicked.connect(self.showLose)
        self.mainScreen.ansRadio3.clicked.connect(self.showLose)
        self.mainScreen.ansRadio4.clicked.connect(self.showLose)

    def showWin(self):
        pass

    def showLose(self):
        pass