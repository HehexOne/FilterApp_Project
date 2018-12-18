#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from ui import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
