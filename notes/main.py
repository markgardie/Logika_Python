from ui.mainWindow import app, mainWindow, uiMainWindow
from logic.notesFunctions import showNotesInfo, addNote, deleteNote, saveNote
from logic.tagFunctions import addTag, deleteTag
from data.dataFunctions import readNotes

notes = readNotes()

uiMainWindow.notesListWidget.itemClicked.connect(lambda: showNotesInfo(notes))
uiMainWindow.createNoteButton.clicked.connect(lambda: addNote(notes))
uiMainWindow.deleteNoteButton.clicked.connect(lambda: deleteNote(notes))
uiMainWindow.saveNoteButton.clicked.connect(lambda: saveNote(notes))
uiMainWindow.addTagButton.clicked.connect(lambda: addTag(notes))
uiMainWindow.deleteTagButton.clicked.connect(lambda: deleteTag(notes))

mainWindow.show()
app.exec_()