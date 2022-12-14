import os
from data.dataFunctions import*
from ui.photoEditorUi import*


ui.folderButton.clicked.connect(showFilenamesList)
ui.photoListWidget.currentRowChanged.connect(imgProcessor.showChosenImage)

mainWindow.show()
app.exec_()