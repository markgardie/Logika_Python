from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator

from MainWindow import MainWindow

# Calculator state.
READY = 0
INPUT = 1

class Calculator(QMainWindow, MainWindow):

    def __init__(self, *args, **kwargs):

        super(Calculator, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton_n0.pressed.connect(lambda: self.input_number(0))
        self.pushButton_n1.pressed.connect(lambda: self.input_number(1))
        self.pushButton_n2.pressed.connect(lambda: self.input_number(2))
        self.pushButton_n3.pressed.connect(lambda: self.input_number(3))
        self.pushButton_n4.pressed.connect(lambda: self.input_number(4))
        self.pushButton_n5.pressed.connect(lambda: self.input_number(5))
        self.pushButton_n6.pressed.connect(lambda: self.input_number(6))
        self.pushButton_n7.pressed.connect(lambda: self.input_number(7))
        self.pushButton_n8.pressed.connect(lambda: self.input_number(8))
        self.pushButton_n9.pressed.connect(lambda: self.input_number(9))

        self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
        # dz