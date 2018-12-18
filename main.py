#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox)
from filters import gotham, kelvin, lomo, nashville
from ui import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image_path = ""
        self.temp_image = ""
        self.open_button.clicked.connect(self.open_image)
        self.save_button.clicked.connect(self.save_image)
        self.kelvin_button.clicked.connect(self.kelvin_filter)
        self.gotham_button.clicked.connect(self.gotham_filter)
        self.lomo_button.clicked.connect(self.lomo_filter)
        self.nashville_button.clicked.connect(self.nashville_filter)

    def open_image(self):
        filt = "Images (*.png *.jpg)"
        self.image_path, _ = QFileDialog.getOpenFileName(self, 'Open your image', filter=filt)


    def save_image(self):
        pass

    def kelvin_filter(self):
        pass

    def lomo_filter(self):
        pass

    def gotham_filter(self):
        pass

    def nashville_filter(self):
        pass


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
