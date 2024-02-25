from PyQt5.QtCore import Qt
from main_screen import MainScreen
from data.notes_dao import NotesDao
from PyQt5.QtWidgets import QWidget, QInputDialog

class NotesScreenManager():

    def __init__(self):

        self.notesDao = NotesDao()
        self.mainScreen = MainScreen()

    def setListeners(self):
        pass

    def createNote(self):
        title, ok = QInputDialog.getText(self.mainScreen, "Додати", "Введіть назву замітки")
        if title != "" and ok:
            self.notesDao.createNote(title)

    def showNotesList(self):
        notesList = self.notesDao.getNotes()
        titleList = []
        


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