from ui.screen_manager import NotesScreenManager
from PyQt5.QtWidgets import QApplication

class Notes(QApplication):

    def __init__(self):
        super().__init__([])
        self.screenManager = NotesScreenManager()
        self.exec_()

app = Notes()