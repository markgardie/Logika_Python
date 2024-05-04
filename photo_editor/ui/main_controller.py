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
        self.mainScreen.leftButton.clicked.connect(self.left)

    def chooseDir(self):
        self.path = QFileDialog.getExistingDirectory()
        self.showPhotoList()

    def showPhotoList(self):
        photoNameList = self.useCase.filterFiles(self.path)
        self.mainScreen.photoListWidget.clear()
        for photo in photoNameList:
            self.mainScreen.photoListWidget.addItem(photo)


    def getImagePath(self):
        if self.mainScreen.photoListWidget.currentRow() >= 0:
            photoName = self.mainScreen.photoListWidget.currentItem().text()
            return self.useCase.open(photoName)

    def showPhoto(self):
        path = self.getImagePath()
        pixmapImage = QPixmap(path)

        pixmapImage = pixmapImage.scaled(
            self.mainScreen.photoLabel.width(),
            self.mainScreen.photoLabel.height(),
            Qt.KeepAspectRatio
        )

    def left(self):
        path = self.getImagePath()
        original = self.useCase.loadImage(path)
        leftImage = self.useCase.left(original)
        self.showPhoto()
        self.useCase.save(path, leftImage)
