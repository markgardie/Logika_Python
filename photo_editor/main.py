import os
from data.dataFunctions import*
from ui.photoEditorUi import*


ui.folderButton.clicked.connect(showFilenamesList)
ui.photoListWidget.currentRowChanged.connect(imgProcessor.showChosenImage)
ui.grayButton.clicked.connect(imgProcessor.blackAndWhite)

mainWindow.show()
app.exec_()