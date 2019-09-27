from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Parameters as Parameters
from openpyxl import Workbook, load_workbook


class FormWidget3(QWidget):

    def __init__(self, parent):

        super(FormWidget3, self).__init__(parent)
        self.setFont(QFont('Century Gothic', 15))
        self.setWindowIcon(QIcon('logo.png'))

        self.art_line = QLineEdit()
        self.art_line.setPlaceHolder('Введите артикул')



        graph_but = QPushButton('График')
        exp_but = QPushButton('Экспортировать')

        hbox = QHBoxLayout()

        self.setLayout(hbox)