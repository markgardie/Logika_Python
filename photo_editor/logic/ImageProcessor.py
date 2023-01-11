import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from ui.photoEditorUi import*
from PIL.ImageFilter import SHARPEN

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

    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        imagePath = os.path.join(self.dir, self.saveDir, self.filename)
        self.showImage(imagePath)

    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        imagePath = os.path.join(self.dir, self.saveDir, self.filename)
        self.showImage(imagePath)

    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        imagePath = os.path.join(self.dir, self.saveDir, self.filename)
        self.showImage(imagePath)

    def sharpen(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        imagePath = os.path.join(self.dir, self.saveDir, self.filename)
        self.showImage(imagePath)


    


