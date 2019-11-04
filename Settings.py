from PyQt5.QtWidgets import *
import Parameters as Parameters
import MainWindow as MainWindow
from PyQt5.QtGui import *


# окно настроек цвета, абсолютно бесполезно, но уже поздно убирать
class Setting(QWidget):

        def __init__(self):
            super(QWidget, self).__init__()

            self.windowW = Parameters.ParameterSize().ww()
            self.windowH = Parameters.ParameterSize().wh()

            self.setWindowTitle('Настройки')
            self.setWindowIcon(QIcon('setting.png'))
            self.setFixedSize(self.windowW * 0.2083333333333333, self.windowH * 0.3703703703703704)
            self.setFont(QFont('Century Gothic', 10))

            self.body()

        def body(self):

            clr_choose = QLabel('Цвет:', self)

            grey_button = QPushButton('Серый', self)
            grey_button.clicked.connect(self.GreyFon)

            pink_button = QPushButton('Розовый', self)
            pink_button.clicked.connect(self.PinkFon)

            olive_button = QPushButton('Оливковый', self)
            olive_button.clicked.connect(self.OliveFon)

            aspid_blue_button = QPushButton('Аспидно-синий', self)
            aspid_blue_button.clicked.connect(self.AspidFon)

            green_button = QPushButton('Темно-бирюзовый', self)
            green_button.clicked.connect(self.GreenFon)

            vbox = QVBoxLayout()
            hbox = QHBoxLayout()

            vbox.addWidget(grey_button)
            vbox.addWidget(pink_button)
            vbox.addWidget(olive_button)
            vbox.addWidget(aspid_blue_button)
            vbox.addWidget(green_button)

            hbox.addWidget(clr_choose)
            hbox.addLayout(vbox)

            self.setLayout(hbox)

        def GreyFon(self):

            self.ButtonColor1 = '#D3D3D3'

            with open("ButtonColor.txt", "w") as colorfile:

                colorfile.write(self.ButtonColor1)

            MainWindow.MainWindow().update()


        def PinkFon(self):

            self.ButtonColor2 = '#CD5C5C'

            with open("ButtonColor.txt", "w") as colorfile:

                colorfile.write(self.ButtonColor2)

            MainWindow.MainWindow().update()

        def OliveFon(self):

            self.ButtonColor3 = '#808000'

            with open("ButtonColor.txt", "w") as colorfile:

                colorfile.write(self.ButtonColor3)

            MainWindow.MainWindow().update()

        def AspidFon(self):

            self.ButtonColor4 = '#6666FF'

            with open("ButtonColor.txt", "w") as colorfile:

                colorfile.write(self.ButtonColor4)

            MainWindow.MainWindow().update()

        def GreenFon(self):

            self.ButtonColor5 = '#336666'

            with open("ButtonColor.txt", "w") as colorfile:

                colorfile.write(self.ButtonColor5)

            MainWindow.MainWindow().update()
