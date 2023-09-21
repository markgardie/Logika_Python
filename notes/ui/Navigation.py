from ui.MainScreen import Ui_MainScreen
from data.NotesRepository import NotesRepository
from PyQt5.QtWidgets import QWidget, QInputDialog
from random import randint

class Navigation():

    def __init__(self):

        self.create_objects()
        self.showNotes()
        self.setListeners()

    def create_objects(self):

        self.mainWidget = QWidget()
        self.mainScreen = Ui_MainScreen()
        self.mainScreen.setupUi(self.mainWidget)

        self.repository = NotesRepository()

        self.mainWidget.show()


    def setListeners(self):

        self.mainScreen.notesListWidget.itemClicked.connect(self.showNoteText)
        self.mainScreen.createNoteBtn.clicked.connect(self.createNote)
        self.mainScreen.saveNoteBtn.clicked.connect(self.saveNote)
        self.mainScreen.deleteNoteBtn.clicked.connect(self.deleteNote)

    def showNotes(self):
        self.repository.readNotes()
        for note in self.repository.notes:
            self.mainScreen.notesListWidget.addItem(note["title"])

    def showNoteText(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        self.mainScreen.noteTextEdit.setText(self.repository.getText(noteTitle))


    def createNote(self):
        noteTitle, ok = QInputDialog.getText(self.mainWidget, "Додати замітку", "Назва замітки: ")
        if ok and noteTitle != "":
            newNote = { 
                        "title" : noteTitle, 
                       "text" : "",
                       "tags": []
                        }
            
            self.mainScreen.notesListWidget.addItem(noteTitle)
            self.repository.createNote(newNote)

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
                


        
