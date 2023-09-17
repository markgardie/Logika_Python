from ui.MainScreen import Ui_MainScreen
from PyQt5.QtWidgets import QWidget, QInputDialog
from data.NotesRepository import NotesRepository

class Navigation():

    def __init__(self):

        self.mainWidget = QWidget()
        self.mainScreen = Ui_MainScreen()
        self.mainScreen.setupUi(self.mainWidget)

        self.repository = NotesRepository()

    def setListeners(self):

        self.mainScreen.createNoteBtn.clicked.connect(self.createNote)

    def showNotesList(self):
        for note in self.repository.notes:
            self.mainScreen.notesListWidget.addItem(note["title"])

    def showText(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text
        for note in self.repository.notes:
            if  note["title"] == noteTitle:
                noteText = note["text"]

        self.mainScreen.noteTextEdit.setText(noteText)

    def createNote(self):
        noteTitle, ok = QInputDialog.getText(self.mainScreen, "Додати нотатку", "Введіть нотатку")


        