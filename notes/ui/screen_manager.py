from ui.main_screen import Ui_MainScreen
from PyQt5.QtWidgets import QWidget, QInputDialog
from data.notes_dao import NotesDao

class NotesScreenManager():

    
    
    def __init__(self):

        self.mainWidget = QWidget()
        self.mainScreen = Ui_MainScreen()
        self.mainScreen.setupUi(self.mainWidget)

        
        self.mainWidget.show()

        
        self.notesDao = NotesDao()

        
        self.showNotesList()
        self.setListeners()

        
    def setListeners(self):

        
        self.mainScreen.createNoteBtn.clicked.connect(self.createNote)
        self.mainScreen.deleteNoteBtn.clicked.connect(self.deleteNote)
        self.mainScreen.saveNoteBtn.clicked.connect(self.saveNote)

        
        self.mainScreen.addTagBtn.clicked.connect(self.addTag)
        self.mainScreen.deleteTagBtn.clicked.connect(self.deleteTag)
        self.mainScreen.searchBtn.clicked.connect(self.search)

        
        self.mainScreen.notesListWidget.itemClicked.connect(self.showNoteInfo)

    
    def showNotesList(self):
        
        notes = self.notesDao.getNotes()

        
        for note in notes:
            self.mainScreen.notesListWidget.addItem(note["title"])

        
    def showNoteInfo(self):
        
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        notes = self.notesDao.getNotes()

        for note in notes:

            if  note["title"] == noteTitle:
                noteText = note["text"]
                self.mainScreen.noteTextEdit.setText(noteText)
                
                
                
                tags = note["tags"]
                self.mainScreen.tagsListWidget.clear()

                for tag in tags:
                    self.mainScreen.tagsListWidget.addItem(tag)

            
    def createNote(self):
        
        noteTitle, ok = QInputDialog.getText(self.mainWidget, "Додати нотатку", "Введіть нотатку")
        
        if ok and noteTitle != "":
            
            self.notesDao.createNote(noteTitle)
            self.mainScreen.notesListWidget.addItem(noteTitle)

    def saveNote(self):
        
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        noteText = self.mainScreen.noteTextEdit.toPlainText()
        
        if noteTitle != "":   
            
            self.notesDao.updateNoteText(noteTitle, noteText)

        
    def deleteNote(self):
        
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        
        if noteTitle != "":
            
            self.notesDao.deleteNote(noteTitle)
            self.mainScreen.notesListWidget.clear()
            self.mainScreen.noteTextEdit.clear()

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
        
        if tag != "":
            
            self.notesDao.deleteTag(noteTitle, tag)

            self.mainScreen.tagsListWidget.clear()
            self.showNoteInfo()

        
    def search(self):
        
        tag = self.mainScreen.searchLineEdit.text()
        if tag != "":

            self.mainScreen.notesListWidget.clear()

            filteredNotes = self.notesDao.search(tag)

            for note in filteredNotes:
                self.mainScreen.notesListWidget.addItem(note["title"])
        
        
        else:
            self.mainScreen.notesListWidget.clear()
            self.showNotesList()




        