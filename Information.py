from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Parameters as Parameters


class Info(QWidget):

        def __init__(self):

                super(QWidget, self).__init__()

                windowW = Parameters.ParameterSize().ww()
                windowH = Parameters.ParameterSize().wh()

                self.setWindowTitle('Информация')
                self.setWindowIcon(QIcon('info.png'))
                self.setFixedSize((windowW)*0.15625, (windowH)* 0.2777777777777778)
                self.setFont(QFont('Century Gothic', 10))

                PrName = QLabel('Книга бизнес-процессов', self)

                Version = QLabel('Версия:  далеко не последняя...', self)

                DevName = QLabel('Разработчики: благородные альтруисты', self)

                CorpName = QLabel("Компания: 'ООО Остеомед-М'", self)

                vbox = QVBoxLayout()

                vbox.addWidget(PrName)
                vbox.addWidget(Version)
                vbox.addWidget(DevName)
                vbox.addWidget(CorpName)
                self.setLayout(vbox)