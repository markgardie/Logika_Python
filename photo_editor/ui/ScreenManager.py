from MainScreen import Ui_MainScreen
from data.ImageRepository import ImageRepository
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class ScreenManager():

    def __init__(self):
        self.mainWidget = QWidget()
        self.mainScreen = Ui_MainScreen()
        self.mainScreen.setupUi(self.mainWidget)

        self.repository = ImageRepository()

    def clickListeners(self):
        self.mainScreen.chooseDirButton.clicked.connect(self.chooseDir)

    
    def chooseDir(self):
        dir = QFileDialog.getExistingDirectory()
        self.repository.setOriginalDir(dir)

    def showPhotoList(self):
        self.mainScreen.photoListWidget.clear()

        photoList = self.repository.filter()

        for photo in photoList:
            self.mainScreen.photoListWidget.addItem(photo)

    def showImage(self):
        if self.mainScreen.photoListWidget.currentRow() >= 0:
            photoName = self.mainScreen.photoListWidget.currentItem().text()
            self.repository.loadImage(photoName)
            path = os.path.join(self.repository.originalDir, photoName)

            self.mainScreen.photoLabel.hide()

            pixmapImage = QPixmap(path)

            width = self.mainScreen.photoLabel.width()
            height = self.mainScreen.photoLabel.height()

            pixmapImage = pixmapImage.scaled(width, height, Qt.KeepAspectRatio)

            self.mainScreen.photoLabel.setPixmap(pixmapImage)

            self.mainScreen.photoLabel.show()

    def blackAndWhite(self):
        self.repository.blackAndWhite()