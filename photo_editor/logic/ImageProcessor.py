import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from ui.photoEditorUi import*

class ImageProcessor():

    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.saveDir = r"C:\Users\Марк\Desktop\Logika_Python\photo_editor\Modified"
    
    def setWorkDir(self, dir):
        self.dir = dir
        
    def loadImage(self, filename):
        self.filename = filename
        imagePath = os.path.join(self.dir, self.filename)
        self.image = Image.open(imagePath)

    def showImage(self, path):
        ui.photoLabel.hide()
        pixmapImage = QPixmap(path)
        w, h = ui.photoLabel.width(), ui.photoLabel.height()
        pixmapImage = pixmapImage.scaled(w, h, Qt.KeepAspectRatio)
        ui.photoLabel.setPixmap(pixmapImage)
        ui.photoLabel.show()

    def showChosenImage(self):

        if ui.photoListWidget.currentRow() >= 0:
            filename = ui.photoListWidget.currentItem().text()
            self.loadImage(filename)
            imagePath = os.path.join(self.dir, self.filename)
            self.showImage(imagePath)


