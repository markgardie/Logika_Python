from PyQt5.QtWidgets import QApplication
from screen_manager import ScreenManager

class MemoryCard(QApplication):

    def __init__(self):
        super().__init__([])
        self.screenManager = ScreenManager()

        self.exec_()

app = MemoryCard()