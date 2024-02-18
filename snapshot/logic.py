from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

import os
import sys
import time

class CameraLogic():

    def select_camera(self, i):
        self.camera = QCamera(self.available_cameras[i])
        self.camera.setCaptureMode(QCamera.CaptureStillImage)

    def take_photo(self):
        pass

    def change_folder(self):
        pass

    def alert(self, message):
        pass