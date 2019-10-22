#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtCore
import Parameters as Parameters
import Doca as Doca
import SendEmail


class SendEmailWindow(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowTitle('Отправка письма')

        windowW1 = Parameters.ParameterSize().ww()
        windowH1 = Parameters.ParameterSize().wh()

        button_color = Parameters.Color().whatcolor()
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(windowW1 * 0.2395833333333333, windowH1 * 0.4259259259259259)

        log_pas = QHBoxLayout()
        btns = QHBoxLayout()
        vbox = QVBoxLayout()

        self.uremail_line = QLineEdit()
        self.uremail_line.setPlaceholderText('Введите ваш @mail')
        self.urpassword_line = QLineEdit()
        self.urpassword_line.setPlaceholderText('Введите ваш пароль')
        self.urpassword_line.setEchoMode(QLineEdit.Password)
        self.address_line = QLineEdit()
        self.address_line.setPlaceholderText('Введите @mail получателя')
        btn_send = QPushButton('Отправить', self)

        btn_send.setStyleSheet("background-color: {0}".format(button_color))

        log_pas.addWidget(self.uremail_line)
        log_pas.addWidget(self.urpassword_line)
        btns.addWidget(btn_send)

        vbox.addLayout(log_pas)
        vbox.addWidget(self.address_line, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(btns)

        self.setLayout(vbox)

        btn_send.clicked.connect(self.send)

    def send(self):

        with open('link.txt', 'r') as f:
            link = f.read()

        uremail = self.uremail_line.text()
        urpassword = self.urpassword_line.text()
        address = self.address_line.text()

        result = SendEmail.send_kom(link, uremail, urpassword, address)

        if result == QMessageBox.Ok:

            self.close()

        else:

            self.close()


class Kom3(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()
        self.link_data = QtCore.pyqtSignal(str)

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle("Коммерческое предложение")

        windowW1 = Parameters.ParameterSize().ww()
        windowH1 = Parameters.ParameterSize().wh()

        button_color = Parameters.Color().whatcolor()
        self.setFixedSize(windowW1 * 0.5, windowH1 * 0.5)

        ets1 = QPushButton('ЭТС Цемент', self)
        ets1.setStyleSheet("background-color: {0}".format(button_color))
        ets1.clicked.connect(self.ets1)

        ets2 = QPushButton('ЭТС Бесцемент. с Мод. Шейкой', self)
        ets2.setStyleSheet("background-color: {0}".format(button_color))
        ets2.clicked.connect(self.ets2)

        ets3 = QPushButton('ЭТС Бесцемент. Моно.', self)
        ets3.setStyleSheet("background-color: {0}".format(button_color))
        ets3.clicked.connect(self.ets3)

        vbox = QVBoxLayout()
        vbox.addWidget(ets1)
        vbox.addWidget(ets2)
        vbox.addWidget(ets3)
        self.setLayout(vbox)


    def ets1(self):
        link = 'кп_3.PDF'
        with open('link.txt', 'w') as f:
            f.write(link)

        self.et1 = SendEmailWindow()
        self.et1.show()


    def ets2(self):
        link = 'кп_1.PDF'
        with open('link.txt', 'w') as f:
            f.write(link)
        self.et2 = SendEmailWindow()
        self.et2.show()

    def ets3(self):
        link = 'кп_3.PDF'
        with open('link.txt', 'w') as f:
            f.write(link)
        self.et3 = SendEmailWindow()
        self.et3.show()


class DocWin(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle("Одноразовый договор")

        windowW1 = Parameters.ParameterSize().ww()
        windowH1 = Parameters.ParameterSize().wh()

        button_color = Parameters.Color().whatcolor()
        self.setFixedSize(windowW1 * 0.5, windowH1 * 0.5)

        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        vbox = QVBoxLayout()

        self.company_line = QLineEdit()
        self.company_line.setPlaceholderText('Представитель')
        self.dir_dol_line = QLineEdit()
        self.dir_dol_line.setPlaceholderText('Должность Представителя')
        self.dir_fio_line = QLineEdit()
        self.dir_fio_line.setPlaceholderText('ФИО Представителя')

        self.adr_line = QLineEdit()
        self.adr_line.setPlaceholderText('Адрес')
        self.tel_line = QLineEdit()
        self.tel_line.setPlaceholderText('Телефон')
        self.inn_line = QLineEdit()
        self.inn_line.setPlaceholderText('ИНН')
        self.email_line = QLineEdit()
        self.email_line.setPlaceholderText('@mail')

        self.r_s_line = QLineEdit()
        self.r_s_line.setPlaceholderText('р/cчёт')
        self.k_s_line = QLineEdit()
        self.k_s_line.setPlaceholderText('к/cчёт')
        self.kpp_line = QLineEdit()
        self.kpp_line.setPlaceholderText('КПП')

        self.bik_line = QLineEdit()
        self.bik_line.setPlaceholderText('БИК')
        self.bank_line = QLineEdit()
        self.bank_line.setPlaceholderText('Банк')

        but = QPushButton("Создать документ", self)
        but.setStyleSheet("background-color: {0}".format(button_color))
        but.clicked.connect(self.ccreate)

        hbox.addWidget(self.company_line)
        hbox.addWidget(self.dir_dol_line)
        hbox.addWidget(self.dir_fio_line)

        hbox2.addWidget(self.adr_line)
        hbox2.addWidget(self.tel_line)
        hbox2.addWidget(self.inn_line)

        hbox3.addWidget(self.r_s_line)
        hbox3.addWidget(self.k_s_line)
        hbox3.addWidget(self.kpp_line)

        hbox4.addWidget(self.bik_line)
        hbox4.addWidget(self.bank_line)
        hbox4.addWidget(self.email_line)

        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addWidget(but, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def ccreate(self):

        company = self.company_line.text()
        dir_dol = self.dir_dol_line.text()
        dir_fio = self.dir_fio_line.text()
        tel = self.tel_line.text()
        adr = self.adr_line.text()
        email = self.email_line.text()
        kpp = self.kpp_line.text()
        r_s = self.r_s_line.text()
        k_s = self.k_s_line.text()
        inn = self.inn_line.text()
        bik = self.bik_line.text()
        bank = self.bank_line.text()

        if company=='' or dir_dol=='' or dir_fio=='' or tel=='' or adr=='' or email=='' or kpp=='' or r_s=='' or k_s=='' or inn=='' or bik=='' or bank=='':

            warning = QMessageBox()
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Возникла ошибка создания документов"
                            ". \nНе заполнены все ячейки")
            warning.setWindowTitle("Ошибка")
            warning.setStandardButtons(QMessageBox.Cancel)

            rslt = warning.exec()

            self.close()

        fam, im, ot = list(dir_fio.split())

        fend = ['ев', 'ёв', 'ов', 'ин', 'он']
        femend = ['ёва', 'ова', 'ева', 'ина', 'она']

        fend2 = ['ый', 'ий']
        femend2 = ['ая', 'ия']

        if fam[-2:] in fend:
            fam1 = fam + 'а '
        elif fam[-3:] in femend:
            fam1 = fam[1:-1] + 'ой '
        elif fam[-2:] in fend2:
            fam1 = fam[1:-2] + 'ого '
        elif fam[-2:] in femend2:
            fam1 = fam[1:-2] + 'ой '
        else:
            fam1 = fam + ' '

        im = im[0] + '.'
        ot = ot[0] + '.'

        way = QFileDialog.getSaveFileName(parent=None, caption="Сохранить разовый договор",
                                          filter="Документ Word (*.docx)")
        filename = way[0]

        fam12 = fam1 + im + ot
        fam22 = fam + ' ' + im + ot

        if Doca.doce(company, dir_dol, fam12, filename, inn, kpp, adr, tel, email, r_s, k_s, bank, bik, fam22) == 0:
            welldone = QMessageBox()
            welldone.setIcon(QMessageBox.Information)
            welldone.setText("Создание договора прошло успешно.")
            welldone.setWindowTitle("Выполнено!")
            welldone.setStandardButtons(QMessageBox.Ok)

            rslt = welldone.exec()

            self.close()

        else:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Возникла ошибка создания документа. \nПроверьте праивльность введенных вами данных.")
            warning.setWindowTitle("Ошибка")
            warning.setStandardButtons(QMessageBox.Cancel)

            rslt = warning.exec()


class FormWidget1(QWidget):

    def __init__(self, parent):

        super(FormWidget1, self).__init__(parent)

        self.setFont(QFont('Century Gothic', 15))
        self.setWindowIcon(QIcon('logo.png'))
        self.button_color = Parameters.Color().whatcolor()

        hbox = QHBoxLayout()

        com_but = QPushButton("Коммерческое предложение", self)
        com_but.setStyleSheet("background-color: {0}".format(self.button_color))
        com_but.clicked.connect(self.three_kom)

        doc_but = QPushButton("Одноразовый договор", self)
        doc_but.setStyleSheet("background-color: {0}".format(self.button_color))
        doc_but.clicked.connect(self.one_doc)

        hbox.addWidget(com_but)
        hbox.addWidget(doc_but)

        self.setLayout(hbox)

    def one_doc(self):

        self.doc = DocWin()
        self.doc.show()

    def three_kom(self):
        self.kom = Kom3()
        self.kom.show()
