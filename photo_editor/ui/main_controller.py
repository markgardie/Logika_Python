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