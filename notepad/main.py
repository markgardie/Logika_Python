import os
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

class MainScreen(QMainWindow):

    def __init__(self):
        super().__init__()

    
    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "Text documents (*.txt);;All files (*.*)",
        )

        if path:
            try:
                with open(path, "r") as file:
                    text = file.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()
