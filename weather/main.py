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

    def update_weather(self):
        worker = WeatherWorker(self.lineEdit.text())
        worker.signals.error.connect(self.alert)
        worker.signals.result.connect(self.weather_result)
        self.thread_pool.start(worker)

    def alert(self, message):
        QMessageBox.warning(self, "Помилка", message)

    def weather_result(self, weather, forecasts):
            self.latitudeLabel.setText("%.2f °" % weather["coord"]["lat"])
            self.longitudeLabel.setText("%.2f °" % weather["coord"]["lon"])

            self.windLabel.setText("%.2f m/s" % weather["wind"]["speed"])

            self.temperatureLabel.setText("%.1f °C" % weather["main"]["temp"])
            self.pressureLabel.setText("%d" % weather["main"]["pressure"])
            self.humidityLabel.setText("%d" % weather["main"]["humidity"])

            self.sunriseLabel.setText(from_ts_to_time_of_day(weather["sys"]["sunrise"]))

            self.weatherLabel.setText(
                "%s (%s)"
                % (
                    weather["weather"][0]["main"],
                    weather["weather"][0]["description"],
                )
            )

            self.set_weather_icon(self.weatherIcon, weather["weather"])

            for n, forecast in enumerate(forecasts["list"][:5], 1):
                getattr(self, "forecastTime%d" % n).setText(from_ts_to_time_of_day(forecast["dt"]))
                self.set_weather_icon(getattr(self, "forecastIcon%d" % n), forecast["weather"])
                getattr(self, "forecastTemp%d" % n).setText("%.1f °C" % forecast["main"]["temp"])

    def set_weather_icon(self, label, weather):
        pixmap = QPixmap(os.path.join("images", "%s.png" % weather[0]["icon"]))
        label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()