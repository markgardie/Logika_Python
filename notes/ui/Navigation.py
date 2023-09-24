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

        self.mainScreen.notesListWidget.itemClicked.connect(self.showText)

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
        if ok and noteTitle != "":
            note = {
                "title": noteTitle,
                "text": "",
                "tags": []
            }

            self.repository.createNote(note)
            self.mainScreen.notesListWidget.addItem(noteTitle)

    def saveNote(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        noteText = self.mainScreen.noteTextEdit.toPlainText()

        self.repository.updateNote(noteTitle, noteText)

    def deleteNote(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        self.repository.deleteNote(noteTitle)
        self.mainScreen.notesListWidget.clear()
        self.mainScreen.noteTextEdit.clear()

        self.showNotesList()

    




        