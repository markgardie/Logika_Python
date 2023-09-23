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
        if ok and noteTitle != "":

            newNote = {
                "title": noteTitle,
                "text": "",
                "tags": []
            }

            self.repository.createNote(newNote)
            self.mainScreen.notesListWidget.addItem(noteTitle)


    def showNotes(self):
        for note in self.repository.readNotes():
            self.mainScreen.notesListWidget.addItem(note["title"])

        
    def showNoteText(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        noteText = self.repository.getText(noteTitle)
        self.mainScreen.noteTextEdit.setText(noteText)

    def saveNote(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        noteText = self.mainScreen.noteTextEdit.toPlainText()

        self.repository.updateNote(noteTitle, noteText)

    def deleteNote(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        self.repository.deleteNote(noteTitle)
        self.mainScreen.notesListWidget.clear()
        self.mainScreen.noteTextEdit.clear()
        self.showNotes()
                

    




