from ui.MainScreen import MainScreen
from data.ImageRepository import ImageRepository
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class ScreenManager():

    def __init__(self):
        self.mainWidget = QWidget()
        self.mainScreen = MainScreen()
        self.mainScreen.setupUi(self.mainWidget)

        self.repository = ImageRepository()

        self.mainWidget.show()

        self.clickListeners()

    def clickListeners(self):
        self.mainScreen.folderButton.clicked.connect(self.chooseDir)
        self.mainScreen.photoListWidget.itemClicked.connect(self.getClickedImageName)
        self.mainScreen.leftButton.clicked.connect(self.left)
        self.mainScreen.rightButton.clicked.connect(self.right)
        self.mainScreen.mirrorButton.clicked.connect(self.mirror)
        self.mainScreen.sharpnessButton.clicked.connect(self.sharpen)
        self.mainScreen.grayButton.clicked.connect(self.blackAndWhite)

    def chooseDir(self):
        self.dir = QFileDialog.getExistingDirectory()
        self.showPhotoList()

    def showPhotoList(self):
        self.mainScreen.photoListWidget.clear()
        photoList = self.repository.filterFiles(self.dir)

        for photo in photoList:
            self.mainScreen.photoListWidget.addItem(photo)

    
    def getClickedImageName(self):
        
        if self.mainScreen.photoListWidget.currentRow() >= 0:

            self.photoName = self.mainScreen.photoListWidget.currentItem().text()
            self.path = os.path.join(self.dir, self.photoName)

            self.showImage()
        
        
    def showImage(self):

        self.mainScreen.photoLabel.hide()

        pixmapImage = QPixmap(self.path)
        width = self.mainScreen.photoLabel.width()
        height = self.mainScreen.photoLabel.height()
        pixmapImage = pixmapImage.scaled(width, height, Qt.KeepAspectRatio)

        self.mainScreen.photoLabel.setPixmap(pixmapImage)

        self.mainScreen.photoLabel.show()


    def left(self):
        image = self.repository.loadImage(self.path)
        modified_image = self.repository.left(image)
        self.path = os.path.join(self.dir, "Modified", self.photoName)
        self.repository.saveImage(modified_image, self.path)

        self.showImage()

    def right(self):
        image = self.repository.loadImage(self.path)
        modified_image = self.repository.right(image)
        self.path = os.path.join(self.dir, "Modified", self.photoName)
        self.repository.saveImage(modified_image, self.path)

        self.showImage()

    def mirror(self):
        image = self.repository.loadImage(self.path)
        modified_image = self.repository.mirror(image)
        self.path = os.path.join(self.dir, "Modified", self.photoName)
        self.repository.saveImage(modified_image, self.path)

        self.showImage()


    def sharpen(self):
        image = self.repository.loadImage(self.path)
        modified_image = self.repository.sharpen(image)
        self.path = os.path.join(self.dir, "Modified", self.photoName)
        self.repository.saveImage(modified_image, self.path)

        self.showImage()

    def blackAndWhite(self):
        image = self.repository.loadImage(self.path)
        modified_image = self.repository.blackAndWhite(image)
        self.path = os.path.join(self.dir, "Modified", self.photoName)
        self.repository.saveImage(modified_image, self.path)

        self.showImage()



            
    
