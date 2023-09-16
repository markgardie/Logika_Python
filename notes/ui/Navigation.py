from ui.MainScreen import Ui_MainScreen
from data.NotesRepository import NotesRepository
from PyQt5.QtWidgets import QWidget

class Navigation():

    def __init__(self):

        self.mainWidget = QWidget()
        self.mainScreen = Ui_MainScreen()
        self.mainScreen.setupUi(self.mainWidget)

        self.repository = NotesRepository()

        self.showNotes()


    def setListeners(self):

        pass

    def showNotes(self):
        self.repository.readNotes()
        self.mainScreen.notesListWidget.addItems(self.repository.notes)

    
