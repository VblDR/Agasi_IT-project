from PyQt5.QtWidgets import *
import Parameters as Parameters
import MainWindow as MainWindow
from PyQt5.QtGui import *


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

            GreyButton = QPushButton('Серый', self)
            GreyButton.clicked.connect(self.GreyFon)

            PinkButton = QPushButton('Розовый', self)
            PinkButton.clicked.connect(self.PinkFon)

            OliveButton = QPushButton('Оливковый', self)
            OliveButton.clicked.connect(self.OliveFon)

            AspidBlueButton = QPushButton('Аспидно-синий', self)
            AspidBlueButton.clicked.connect(self.AspidFon)

            GreenButton = QPushButton('Темно-бирюзовый', self)
            GreenButton.clicked.connect(self.GreenFon)

            vbox = QVBoxLayout()
            hbox = QHBoxLayout()

            vbox.addWidget(GreyButton)
            vbox.addWidget(PinkButton)
            vbox.addWidget(OliveButton)
            vbox.addWidget(AspidBlueButton)
            vbox.addWidget(GreenButton)

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
