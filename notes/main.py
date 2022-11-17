from ui.mainWindow import app, mainWindow, uiMainWindow
from logic.notesFunctions import showNotesInfo, addNote, deleteNote, saveNote
from data.dataFunctions import readNotes

notes = readNotes()

uiMainWindow.notesListWidget.itemClicked.connect(lambda: showNotesInfo(notes))
uiMainWindow.createNoteButton.clicked.connect(lambda: addNote(notes))
uiMainWindow.deleteNoteButton.clicked.connect(lambda: deleteNote(notes))
uiMainWindow.saveNoteButton.clicked.connect(lambda: saveNote(notes))

mainWindow.show()
app.exec_()