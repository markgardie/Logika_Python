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

    def updateNoteText(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        newText = self.mainScreen.noteTextEdit.text()
        
        self.notesDao.updateNoteText(noteTitle, newText)

    def deleteNote(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()

        self.notesDao.deleteNote(noteTitle)
        self.mainScreen.notesListWidget.clear()
        self.showNotesList()

    def addTag(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        tag = self.mainScreen.searchLineEdit.text()
        
        if tag != "":
            self.notesDao.addTag(noteTitle, tag)
            self.mainScreen.tagsListWidget.addItem(tag)

    def deleteTag(self):
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        tag = self.mainScreen.tagsListWidget.selectedItems()[0].text()

        self.notesDao.deleteTag(noteTitle, tag)
        self.mainScreen.tagsListWidget.clear()
        self.showNoteInfo()


    def search(self):
        searchTag = self.mainScreen.searchLineEdit.text()
        self.mainScreen.notesListWidget.clear()

        if searchTag != "":
            filteredNotes = self.notesDao.search(searchTag)
            for note in filteredNotes:
                self.mainScreen.notesListWidget.addItem(note)
        else:
            self.showNotesList()
