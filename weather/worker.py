import json
from urllib.parse import urlencode

import constants
import requests
from PyQt6.QtCore import (
    QObject,
    QRunnable,
    pyqtSignal,
    pyqtSlot,
)



class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(dict, dict)

class WeatherWorker(QRunnable):
    signals = WorkerSignals()
    is_interrupted = False

    def __init__(self, location):
        super().__init__()
        self.location = location

    @pyqtSlot
    def run(self):
        pass