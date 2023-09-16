from ui.MainScreen import Ui_MainScreen
from data.NotesRepository import NotesRepository
from PyQt5.QtWidgets import QWidget, QInputDialog

class Navigation():

    def __init__(self):
        
        self.mainWidget = QWidget()
        self.mainScreen = Ui_MainScreen()
        self.mainScreen.setupUi(self.mainWidget)

        self.repository = NotesRepository()

    def createNote(self):
        noteTitle, ok = QInputDialog.getText(self.mainScreen, "Додати нотатку", "Назва нотатки:")

