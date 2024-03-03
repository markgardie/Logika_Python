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

        for note in notesList:
            titleList.append(note["title"])

        for title in titleList:
            self.mainScreen.notesListWidget.addItem(title)

    
    def showNoteInfo(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        notes = self.notesDao.getNotes()

        for note in notes:
            if note["title"] == noteTitle:
                self.mainScreen.noteTextEdit.setText(note["text"])

                self.mainScreen.tagsListWidget.clear()
                for tag in note["tags"]:
                    self.mainScreen.tagsListWidget.addItem(tag)

    def updateNoteText(self, title, newText):

        pass

    def deleteNote(self):
        
        pass

    def addTag(self):
        pass

    def deleteTag(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        tag = self.mainScreen.tagsListWidget.selectedItems()[0].text()

        self.notesDao.deleteTag(noteTitle, tag)

    def search(self):
        