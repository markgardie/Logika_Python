from PyQt5.QtCore import Qt
from main_screen import MainScreen
from data.notes_dao import NotesDao

class ScreenManager():

    def __init__(self):

        self.notesDao = NotesDao()

    def setListeners(self):
        pass

    def createNote(self, title):
        pass

    def showNotes(self):
        pass

    def updateNoteText(self, title, newText):

        pass

    def deleteNote(self, deleteTitle):
        
        pass

    def addTag(self, title, tag):
        pass

    def deleteTag(self):
        pass


