import os
from data.dataFunctions import*
from ui.photoEditorUi import*

ui.folderButton.clicked.connect(showFilenamesList)

mainWindow.show()
app.exec_()