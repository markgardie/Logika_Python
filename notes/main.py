from ui.mainWindow import app, mainWindow, ui
from logic.notesFunctions import showNotesInfo, addNote, deleteNote, saveNote
from logic.tagFunctions import addTag, deleteTag, searchByTag
from data.dataFunctions import readNotes

notes = readNotes()

ui.notesListWidget.itemClicked.connect(lambda: showNotesInfo(notes))
ui.createNoteButton.clicked.connect(lambda: addNote(notes))
ui.deleteNoteButton.clicked.connect(lambda: deleteNote(notes))
ui.saveNoteButton.clicked.connect(lambda: saveNote(notes))
ui.addTagButton.clicked.connect(lambda: addTag(notes))
ui.deleteTagButton.clicked.connect(lambda: deleteTag(notes))
ui.tagSearchButton.clicked.connect(lambda: searchByTag(notes))

mainWindow.show()
app.exec_()