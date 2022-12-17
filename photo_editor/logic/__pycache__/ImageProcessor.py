import os
from PIL import Image, ImageFilter
from ui.photoEditorUi import *
from PyQt5.QtGui import QPixmap

class ImageProcessor():

    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.saveDir = "Modified"

    def setDir(self, dir):
        self.dir = dir

    def loadImage(self, filename):
        self.filename = filename
        imagePath = os.path.join(self.dir, filename)
        self.image = Image.load(imagePath)

    def showImage(self):
        ui.photoLabel.clear()
        pixmapImage = QPixmap()
        w = ui.photoLabel.width()
        h = ui.photoLabel.height()
        pixmapImage = pixmapImage.scaled(w, h)
        ui.photoLabel.setPixmap(pixmapImage)
        ui.photoLabel.show()

    def showChosenImage(self):
        if ui.photoListWidget.currentRow() > 0:
            
