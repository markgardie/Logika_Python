from MainScreen import Ui_MainScreen
from data.ImageRepository import ImageRepository
from PyQt5.QtWidgets import QWidget, QFileDialog

class ScreenManager():

    def __init__(self):
        self.mainWidget = QWidget()
        self.mainScreen = Ui_MainScreen()
        self.mainScreen.setupUi(self.mainWidget)

        self.repository = ImageRepository()

    def clickListeners(self):
        self.mainScreen.chooseDirButton.clicked.connect(self.chooseDir)

    
    def chooseDir(self):
        dir = QFileDialog.getExistingDirectory()
        self.repository.setOriginalDir(dir)