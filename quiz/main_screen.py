from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton
 
class MainScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генератор чисeл")
        self.resize(800, 600)

        self.createWidgets()
        self.createLayouts()
        self.setupScreen()

    def createWidgets(self):
        pass

    def createLayouts(self):
        pass

    def setupScreen(self):

        pass