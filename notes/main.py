from ui.mainWindow import app, mainWindow, uiMainWindow
from logic.functions import showNotesInfo, addNote
from data.data import readNotes

notes = readNotes()

uiMainWindow.notesListWidget.itemClicked.connect(lambda: showNotesInfo(notes))
uiMainWindow.createNoteButton.clicked.connect(lambda: addNote(notes))

mainWindow.show()
app.exec_()