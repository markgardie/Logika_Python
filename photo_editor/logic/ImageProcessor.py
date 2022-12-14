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
        self.saveDir = r"Modified"
    
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

    
    def saveImage(self):
       path = os.path.join(self.dir, self.saveDir)
       if not(os.path.exists(path) or os.path.isdir(path)):
           os.mkdir(path)
       imagePath = os.path.join(path, self.filename)
       self.image.save(imagePath)


    def blackAndWhite(self):
       self.image = self.image.convert("L")
       self.saveImage()
       imagePath = os.path.join(self.dir, self.saveDir, self.filename)
       self.showImage(imagePath)

    


