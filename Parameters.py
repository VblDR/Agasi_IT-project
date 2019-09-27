from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ParameterSize():

        def __init__(self):
            window_size = QDesktopWidget().availableGeometry()
            self.window_weight = window_size.width()
            self.window_height = window_size.height()

        def ww(self):
            return self.window_weight

        def wh(self):
            return self.window_height


class Color():

        def __init__(self):

            with open("ButtonColor.txt", "r") as colorfile:
                self.colourfon = colorfile.read()

        def whatcolor(self):

            return self.colourfon