from ui.MainScreen import Ui_MainScreen
from PyQt5.QtWidgets import QWidget

class Navigation():

    def __init__(self):

        self.mainScreen = QWidget()
        mainScreenSetup = Ui_MainScreen()
        mainScreenSetup.setupUi(self.mainScreen)

        self.mainScreen.show()

    def setListeners(self):

        pass


        