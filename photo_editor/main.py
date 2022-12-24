import os
from data.dataFunctions import*
from ui.photoEditorUi import*
from logic.ImageProcessor import ImageProcessor

imgProcessor = ImageProcessor()

ui.folderButton.clicked.connect(showFilenameList)
ui.photoListWidget.currentRowChanged.connect(imgProcessor.showChosenImage)
ui.grayButton.clicked.connect(imgProcessor.blackAndWhite)

mainWindow.show()
app.exec_()