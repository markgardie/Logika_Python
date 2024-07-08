import os
import sys

from MainWindow import Ui_MainWindow
from PyQt6.QtCore import (
    QThreadPool,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
)
from utils import from_ts_to_time_of_day
from workers import WeatherWorker

class MainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.update_weather)

        self.thread_pool = QThreadPool()

        self.show()