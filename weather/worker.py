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

    def __init__(self):
        super().__init__()
        self.finished = pyqtSignal()
        self.success = pyqtSignal(dict, dict)
        self.error = pyqtSignal(str)

class WeatherWorker(QRunnable):
    
    def __init__(self, location):
        super().__init__()
        self.location = location
        self.is_interrupted = False
        self.signals = WorkerSignals()

    def run(self):
        try:
            params = dict(q=self.location, appid=constants.OPENWEATHERMAP_API_KEY)

            url = "http://api.openweathermap.org/data/2.5/weather?%s&units=metric" % urlencode(params)
            resp = requests.get(url)
            weather = json.loads(resp.text)

            if resp.status_code != 200:
                raise Exception(weather["message"])
            
            url = "http://api.openweathermap.org/data/2.5/forecast?%s&units=metric" % urlencode(params)
            r = requests.get(url)
            forecast = json.loads(r.text)

            self.signals.success.emit(weather, forecast)
        except Exception as e:
            self.signals.error.emit(str(e))

        self.signals.finished.emit()


       



