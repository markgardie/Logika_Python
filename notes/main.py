from ui.mainWindow import app, mainWindow, uiMainWindow
from data.greetings import loadNotes, showNotes

loadNotes()

uiMainWindow.notesListWidget.itemClicked.connect(showNotes)

mainWindow.show()
app.exec_()