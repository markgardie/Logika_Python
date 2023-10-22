from ScreenManager import ScreenManager
from PyQt5.QtWidgets import QApplication

class ImageEditorApp(QApplication):

    def __init__(self):
        super().__init__([])
        screenManager = ScreenManager()


app = ImageEditorApp()