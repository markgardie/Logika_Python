import os
from data.dataFunctions import*
from ui.photoEditorUi import*


ui.folderButton.clicked.connect(showFilenamesList)
ui.photoListWidget.currentRowChanged.connect(imgProcessor.showChosenImage)
ui.grayButton.clicked.connect(imgProcessor.blackAndWhite)
ui.leftButton.clicked.connect(imgProcessor.left)
ui.rightButton.clicked.connect(imgProcessor.right)
ui.mirrorButton.clicked.connect(imgProcessor.mirror)
ui.sharpnessButton.clicked.connect(imgProcessor.sharpen)

mainWindow.show()
app.exec_()