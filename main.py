#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog)
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageEnhance
from ui import Ui_MainWindow
from shutil import copy


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
        self.buttons = [self.save_button, self.kelvin_button, self.gotham_button, self.lomo_button,
                        self.nashville_button, self.brightness_dial, self.contrast_dial, self.color_dial]

        self.brightness = 50
        self.color = 50
        self.contrast = 50

        self.brightness_dial.mouseReleaseEvent = self.brightness_dial_event
        self.brightness_dial.keyReleaseEvent = self.brightness_dial_event_stay

        self.color_dial.mouseReleaseEvent = self.color_dial_event
        self.color_dial.keyReleaseEvent = self.color_dial_event_stay

        self.contrast_dial.mouseReleaseEvent = self.contrast_dial_event
        self.contrast_dial.keyReleaseEvent = self.contrast_dial_event_stay

        for i in self.buttons:
            i.setEnabled(False)

    # Applying filter function, accepts filter and saving image to temp location
    def apply_filter(self, filt):
        if filt is None:
            img = Image.open(self.image_path)
            img.save(self.temp_image)
            img.close()
            return
        img = Image.open(self.image_path)
        img = img.filter(filt)
        img = ImageEnhance.Brightness(img).enhance(self.brightness / 50)
        img = ImageEnhance.Color(img).enhance(self.color / 50)
        img = ImageEnhance.Contrast(img).enhance(self.contrast / 50)
        img.save(self.temp_image)
        img.close()

    # Reloading image in image_label
    def reload_image(self):
        pixmap = QPixmap(self.temp_image).scaled(self.image_label.size(), Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)

    # Copy file to temp location (For opening)
    def copy_to_tmp(self):
        copy(self.image_path, "tmp/")
        self.temp_image = "tmp/" + self.image_path.split("/")[-1]

    # Open image with QFileDialog
    def open_image(self):
        filt = "Images (*.png *.jpg)"
        tmp_img = self.image_path
        self.image_path, _ = QFileDialog.getOpenFileName(self, 'Open your image', filter=filt)
        if self.image_path == '':
            self.image_path = tmp_img
            return
        self.copy_to_tmp()
        self.reload_image()
        for i in self.buttons:
            i.setEnabled(True)

    # Save image with QFileDialog
    def save_image(self):
        filt = "Images (*.png *.jpg)"
        tmp_img = self.image_path
        self.image_path, _ = QFileDialog.getSaveFileName(self, 'Save your image', filter=filt)
        if self.image_path == '':
            self.image_path = tmp_img
            return
        copy(self.temp_image, self.image_path)

    # Filter on button Kelvin
    def kelvin_filter(self):
        self.apply_filter(ImageFilter.EMBOSS)
        self.reload_image()

    # Filter on button LOMO
    def lomo_filter(self):
        self.apply_filter(ImageFilter.CONTOUR)
        self.reload_image()

    # Filter on button Gotham
    def gotham_filter(self):
        self.apply_filter(ImageFilter.EDGE_ENHANCE_MORE)
        self.reload_image()

    # Cancel filter button
    def nashville_filter(self):
        self.apply_filter(None)
        self.reload_image()
        self.brightness = 50
        self.color = 50
        self.contrast = 50
        self.brightness_dial_event_stay("")
        self.color_dial_event_stay("")
        self.contrast_dial_event_stay("")

    # Brightness mouse event
    def brightness_dial_event(self, e):
        self.brightness = self.brightness_dial.value()
        img = ImageEnhance.Brightness(Image.open(self.image_path)).enhance(self.brightness / 50)
        img = ImageEnhance.Color(img).enhance(self.color / 50)
        img = ImageEnhance.Contrast(img).enhance(self.contrast / 50)
        img.save(self.temp_image)
        img.close()
        self.reload_image()

    # Don't use keyboard, please
    def brightness_dial_event_stay(self, e):
        self.brightness_dial.setValue(self.brightness)

    # Color mouse event
    def color_dial_event(self, e):
        self.color = self.color_dial.value()
        img = ImageEnhance.Brightness(Image.open(self.image_path)).enhance(self.brightness / 50)
        img = ImageEnhance.Color(img).enhance(self.color / 50)
        img = ImageEnhance.Contrast(img).enhance(self.contrast / 50)
        img.save(self.temp_image)
        img.close()
        self.reload_image()

    # Don't use keyboard, please
    def color_dial_event_stay(self, e):
        self.color_dial.setValue(self.color)

    # Contrast mouse event
    def contrast_dial_event(self, e):
        self.contrast = self.contrast_dial.value()
        img = ImageEnhance.Brightness(Image.open(self.image_path)).enhance(self.brightness / 50)
        img = ImageEnhance.Color(img).enhance(self.color / 50)
        img = ImageEnhance.Contrast(img).enhance(self.contrast / 50)
        img.save(self.temp_image)
        img.close()
        self.reload_image()

    # Don't use keyboard, please
    def contrast_dial_event_stay(self, e):
        self.contrast_dial.setValue(self.contrast)


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
