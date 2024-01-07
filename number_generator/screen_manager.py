from main_screen import MainScreen
from random import randint

class ScreenManager():

    def __init__(self):

        self.mainScreen = MainScreen()

        self.mainScreen.show()

        self.clickListeners()

    def clickListeners(self):
        self.mainScreen.generateButton.clicked.connect(self.generateNumber)
    
    def generateNumber(self):
        num = randint(1, 100)
        self.mainScreen.numberLabel.setText(str(num))
        
  