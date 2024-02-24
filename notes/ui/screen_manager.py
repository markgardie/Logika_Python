from PyQt5.QtCore import Qt
from main_screen import MainScreen
from data.notes_dao import NotesDao
from PyQt5.QtWidgets import QWidget, QInputDialog

class ScreenManager():

    def __init__(self):

        self.notesDao = NotesDao()

    def setListeners(self):
        pass

    def createNote(self):
        
        noteTitle, ok = QInputDialog.getText(
            self.mainScreen, 
            "Додатки нотатку", 
            "Введіть назву нотатки"
        )

        if noteTitle != "" and ok:
            self.notesDao.createNote(noteTitle)

    def showNotesList(self):

        notesList = self.notesDao.getNotes()
        titleList = []

        for note in notesList:
            titleList.append(note["title"])

        for title in titleList:
            self.mainScreen.notesListWidget.addItem(title)


    def showNoteText(self):
        pass

    def updateNoteText(self, title, newText):

        pass

    def deleteNote(self, deleteTitle):
        
        pass

    def addTag(self, title, tag):
        pass

    def deleteTag(self):
        pass


