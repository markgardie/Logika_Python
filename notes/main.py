from ui.mainWindow import app, mainWindow, uiMainWindow
from logic.functions import showNotesList, showNotesInfo

showNotesList()

uiMainWindow.notesListWidget.itemClicked.connect(showNotesInfo)

mainWindow.show()
app.exec_()