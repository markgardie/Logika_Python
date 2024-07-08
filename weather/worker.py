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

    def __init__(self, location):
        super().__init__()
        self.location = location
        self.signals = WorkerSignals()
        self.is_interrupted = False

    @pyqtSlot
    def run(self):
        try:
            params = dict(q=self.location, appid=constants.OPENWEATHERMAP_API_KEY)
            url = "http://api.openweathermap.org/data/2.5/weather?%s&units=metric" % urlencode(params)
            r = requests.get(url)
            weather = json.loads(r.text)

            if r.status_code != 200:
                raise Exception(weather["message"])
            

            self.signals.result.emit(weather, forecast)

        except Exception as e:
            self.signals.error.emit(str(e))

        self.signals.finished.emit()