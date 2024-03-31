from ui.main_screen import MainScreen
from domain.edit_photo_use_case import EditPhotoUseCase
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class MainController():

    def __init__(self):
        self.mainScreen = MainScreen()
        self.useCase = EditPhotoUseCase()

    def clickListeners(self):
        pass

    def chooseDir(self):
        self.path = QFileDialog.getExistingDirectory()
        self.showPhotoList()

    def showPhotoList(self):
        filtersFiles = self.useCase.filterFiles(self.path)
        self.mainScreen.photoListWidget.clear()
        for file in filtersFiles:
            self.mainScreen.photoListWidget.addItem(file)

    def getImagePath(self):
        if self.mainScreen.photoListWidget.currentRow() >= 0:
            photoName = self.mainScreen.photoListWidget.currentItem.text()
            return self.useCase.open(photoName)

    def showPhoto(self):
        path = self.getImagePath()
        pixmapImage = QPixmap(path)

        width = self.mainScreen.photoLabel.width()
        height = self.mainScreen.photoLabel.height()

        pixmapImage = pixmapImage.scaled(width, height, Qt.KeepAspectRatio)

        self.mainScreen.photoLabel.setPixmap(pixmapImage)
        self.mainScreen.photoLabel.show()

    def left(self):
        path = self.getImagePath()
        original = self.useCase.loadImage(path)
        leftImage = self.useCase.left(original)
        self.useCase.save(path, leftImage)
        self.showPhoto()

        
