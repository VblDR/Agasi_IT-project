from PyQt5.QtWidgets import *


# модуль пользовательских настроек

# настройки разрешени€ экрана
class ParameterSize():

        def __init__(self):
            window_size = QDesktopWidget().availableGeometry()
            self.window_weight = window_size.width()
            self.window_height = window_size.height()

        def ww(self):
            return self.window_weight

        def wh(self):
            return self.window_height


# настройки цвета кнопок
# второе по бесполезности мое создание в этом проекте... сразу после самого проекта, разумеетс€
class Color():

        def __init__(self):

            with open("ButtonColor.txt", "r") as colorfile:
                self.colourfon = colorfile.read()

        def whatcolor(self):

            return self.colourfon