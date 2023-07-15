from PyQt5.QtWidgets import QWidget

class BaseScreen(QWidget):

    def __init__(self, width, height, title):
        super().__init__()

        self.resize(width, height)
        self.setWindowTitle(title) 