from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Parameters as Parameters


# окно информации
# ничего примечательного... если что-то и сломалось, то не оно ему виной, поверь
class Info(QWidget):

        def __init__(self):

                super(QWidget, self).__init__()

                window_w = Parameters.ParameterSize().ww()
                window_h = Parameters.ParameterSize().wh()

                self.setWindowTitle('Информация')
                self.setWindowIcon(QIcon('info.png'))
                self.setFixedSize(window_w * 0.15625, window_h * 0.2777777777777778)
                self.setFont(QFont('Century Gothic', 10))

                pr_name = QLabel('Книга бизнес-процессов', self)
                version = QLabel('Версия:  далеко не последняя...', self)
                dev_name = QLabel('Разработчики: благородные альтруисты', self)
                corp_name = QLabel("Компания: 'ООО Остеомед-М'", self)

                vbox = QVBoxLayout()
                vbox.addWidget(pr_name)
                vbox.addWidget(version)
                vbox.addWidget(dev_name)
                vbox.addWidget(corp_name)
                self.setLayout(vbox)
