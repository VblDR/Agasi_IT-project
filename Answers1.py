#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import Parameters as Parameters
import SendEmail as SendEmail
import pyperclip


# Класс кнопки для копирования ответа (часто используется, поэтоу был создан отдельный класс)
class CopyButton():

    def button(self):

        copy_button = QPushButton('Скопировать текст', self)
        button_color = Parameters.Color().whatcolor()
        copy_button.setStyleSheet("background-color: {0}".format(button_color))
        return copy_button


# Класс кнопки для отправки письма (часто используется, поэтоу был создан отдельный класс)
class SendEmailButton():

    def button(self):

        send_button = QPushButton('Отправить письмо', self)
        button_color = Parameters.Color().whatcolor()
        send_button.setStyleSheet("background-color: {0}".format(button_color))
        return send_button


# Класс окна отправки письма
class SendEmailWindow(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowTitle('Отправка письма')
        windoww1 = Parameters.ParameterSize().ww()
        windowh1 = Parameters.ParameterSize().wh()
        button_color = Parameters.Color().whatcolor()
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(windoww1 * 0.2395833333333333, windowh1 * 0.4259259259259259)

        log_pas = QHBoxLayout()
        btns = QHBoxLayout()
        vbox = QVBoxLayout()

        # поле ввода почты
        self.uremail_line = QLineEdit()
        self.uremail_line.setPlaceholderText('Введите ваш @mail')
        # поле ввода пароля
        self.urpassword_line = QLineEdit()
        self.urpassword_line.setPlaceholderText('Введите ваш пароль')
        self.urpassword_line.setEchoMode(QLineEdit.Password)
        # поле ввода почты адресата
        self.address_line = QLineEdit()
        self.address_line.setPlaceholderText('Введите @mail получателя')
        # кнопка отправки
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

        uremail = self.uremail_line.text()
        urpassword = self.urpassword_line.text()
        address = self.address_line.text()

        result = SendEmail.send_letter(uremail, urpassword, address)

        if result == QMessageBox.Ok:

            self.close()

        else:

            self.close()


'''

Далее идут шаблонные ответы. Они занимают порядка 2000 строк, поэтому рекомендую не тратить время на чтение их всех,
так как структура каждого из них идентична. Предлагаю рассмотреть реализацию одного из овтетов на примере ниже.

'''


# Класс первого раздела
class Ans1(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        # Настрйоки интерфейса окна
        button_color = Parameters.Color().whatcolor()
        self.setFont(QFont('Century Gothic', 10))
        windoww1 = Parameters.ParameterSize().ww()
        windowh1 = Parameters.ParameterSize().wh()
        self.setWindowTitle('Вопросы по заказу продукции')
        self.setFixedSize(windoww1*0.625, windowh1*0.7407407407407407)
        self.setWindowIcon(QIcon('logo.png'))

        # Далее идут подразделы этой тематики, реализованные кнопками,
        # нажав на которые, пользователь попадет в этот подраздел
        topleft1 = QPushButton("Обращается новый партнёр "
                               "\nи хочет узнать, каким образом "
                               "\nможно приобрести продукцию Остеомеда.", self)
        topleft1.setStyleSheet("background-color: {0}".format(button_color))
        topleft1.clicked.connect(self.show_tema13)

        topleft2 = QPushButton("Партнёр хочет сделать заказ "
                               "\nне стандартной продукции"
                               "\n(с индивидуальными характеристиками).", self)
        topleft2.setStyleSheet("background-color: {0}".format(button_color))
        topleft2.clicked.connect(self.show_tema14)

        topleft3 = QPushButton("Партнёр просит принять "
                               "\nего заказ по телефону,"
                               "\nт.к. нет возможности написать письмо. ", self)
        topleft3.setStyleSheet("background-color: {0}".format(button_color))
        topleft3.clicked.connect(self.show_tema18)

        topleft4 = QPushButton("Партнёр просит уточнить, "
                               "\nвозможна ли срочная поставка товара"
                               "\n(день в день) и что для этого требуется. ", self)
        topleft4.setStyleSheet("background-color: {0}".format(button_color))
        topleft4.clicked.connect(self.show_tema12)

        topleft5 = QPushButton("Партнёр просит скорректировать счёт на продукцию"
                               "\nпо прошествии более трёх дней с даты полной или частичной оплаты"
                               "\n(продукции нет в наличии,"
                               "\nона будет специально производиться для партнёра).", self)
        topleft5.setStyleSheet("background-color: {0}".format(button_color))
        topleft5.clicked.connect(self.show_tema11)

        # Компануем подразделы в окне
        vbox = QVBoxLayout()
        vbox.addWidget(topleft1)
        vbox.addWidget(topleft2)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(topleft3)
        vbox2.addWidget(topleft4)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addLayout(vbox2)
        hbox.addWidget(topleft5)

        self.setLayout(hbox)

    # Функции вызова окон с ответами
    def show_tema13(self):
        self.w11 = Tema13()
        self.w11.show()

    def show_tema14(self):
        self.w12 = Tema14()
        self.w12.show()

    def show_tema18(self):
        w13 = Tema18()
        self.w13.show()

    def show_tema12(self):
        self.w14 = Tema12()
        self.w14.show()

    def show_tema11(self):
        self.w15 = Tema11()
        self.w15.show()


# Ответ на первый подраздел
class Tema13(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        # Настрйоки интерфейса окна
        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()
        self.title = 'Приобретение продукции'
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle(self.title)
        self.setFont(QFont('Century Gothic', 10))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        # Ответ
        self.txt = "Последовательность действий следующая:" \
                   "\n1) Необходимо уточнить название или регион конечного клиента." \
                   "\n2) Перенаправить к менеджеру по указанному региону, что бы менеджер решил:" \
                   "\n -Самому работать с данной больницей" \
                   "\n  (работа с больницей напрямую – скорее исключение, при особой необходимости для компании)." \
                   "\n -Отдать уже существующему дилеру (чаще всего просто передаётся существующему дилеру)." \
                   "\n -Если в этом регионе нет работающего дилера, то необходимо" \
                   "\n  запрашивать у нового дилера все документы для заключения с ним договора поставки." \
                   "\nВажно так же учитывать о какой сумме идет речь, " \
                   "\n насколько долгосрочное это будет сотрудничество " \
                   "\n и имеет ли смысл вообще заключать с новым юр. лицом какое-либо соглашение. "

        answer1_1 = QLabel(self.txt, self)

        # Кнопка отправки
        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        # Кнопка копирования
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        # Компануем объекты в окне
        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_1, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    # функция подготовки данных для отправки письма
    def show_send(self):

        # Вызов окна отправки для ввода реквизитов
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        # Записываем ответ во временный файл
        with open("Text.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.txt)
        # Записываем подраздел во временный файл
        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    # Функция копирования Ответа
    def copy(self):

        pyperclip.copy(self.txt)


class Tema14(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setWindowIcon(QIcon('logo.png'))
        self.setFont(QFont('Century Gothic', 10))

        self.title = 'Заказ нестандартной продукции'

        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Последовательность действий следующая:' \
                   '\n1) Стараемся предложить все-таки то,' \
                   '\nчто имеется на складе с пояснением преимуществ стандартного изделия ' \
                   '\n(особенно указывая на то, что оно либо уже есть на складах, ' \
                   '\nлибо будет сделано гораздо быстрее и дешевле индивидуального заказа).' \
                   '\n2) Уточняем у руководства и производства, ' \
                   '\nможно ли сделать такое индивидуальное изделие для партнёра.' \
                   '\n3) Если партнёр на 100% хочет индивидуальное изделие - уточняем конечного клиента,' \
                   '\nинформируем о большем времени изготовления и большей стоимости изготовления ' \
                   '\n(а также предупреждаем о том, что на продукцию будет распространяться ставка НДС 18%),' \
                   '\nинформируем о необходимости 100% предоплаты. ' \
                   '\n4) Ждём предоплаты и после согласовываем заказ с производством.'

        answer1_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):

        pyperclip.copy(self.txt)


class Tema18(QWidget):

    def __init__(self):

        button_color = Parameters.Color().whatcolor()

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()
        self.setWindowIcon(QIcon('logo.png'))
        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Заказ по телефону')

        self.setFixedSize(window_w1 * 0.5208333333333333, window_h1 * 0.6481481481481481)

        topleft1 = QPushButton("Надёжный, проверенный партнёр и ситуация исключительной важности:", self)
        topleft1.setStyleSheet("background-color: {0}".format(button_color))
        topleft1.clicked.connect(self.show_tema181)

        topleft2 = QPushButton("Во всех остальных случаях:", self)
        topleft2.setStyleSheet("background-color: {0}".format(button_color))
        topleft2.clicked.connect(self.show_tema182)

        hbox = QHBoxLayout()
        hbox.addWidget(topleft1)
        hbox.addWidget(topleft2)

        self.setLayout(hbox)

    def show_tema181(self):

        self.w11 = Tema181()
        self.w11.show()

    def show_tema182(self):
        self.w12 = Tema182()
        self.w12.show()


class Tema181(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.title = "Заказ по телефону (надежный парнер, частный случай)"

        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Возможно исключение в виде заказа по телефону ' \
                   '\n(с одновременной трансляцией письма партнёру с указанием того, ' \
                   '\nчто заказ принят по телефону).'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema182(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.title = 'Заказ по телефону (остальные случаи)'

        self.setWindowTitle('Остальные случаи')

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Принятие заявки на продукцию по телефону не представляется возможным.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema12(QWidget):

    def __init__(self):

        button_color = Parameters.Color().whatcolor()

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle('Срочная доставка')

        self.setFixedSize(window_w1 * 0.5208333333333333, window_h1 * 0.6481481481481481)

        topleft1 = QPushButton("Товар есть на складе в г. Москва:", self)
        topleft1.setStyleSheet("background-color: {0}".format(button_color))
        topleft1.clicked.connect(self.show_tema121)

        topleft2 = QPushButton("Товара нет на складе в г. Москва:", self)
        topleft2.setStyleSheet("background-color: {0}".format(button_color))
        topleft2.clicked.connect(self.show_tema122)

        hbox = QHBoxLayout()
        hbox.addWidget(topleft1)
        hbox.addWidget(topleft2)

        self.setLayout(hbox)

    def show_tema121(self):

        self.w11 = Tema121()
        self.w11.show()

    def show_tema122(self):
        self.w12 = Tema122()
        self.w12.show()


class Tema121(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.title = 'Срочная доставка (товар есть)'
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Срочная поставка можна при заказе до 15:00 и 100% оплате выставленного счёта.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema122(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.title = 'Срочная доставка (товара нет)'
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Объяснить клиенту, что невозможно день-в-день доставить товар с производства в Москву.' \
                   '\nМинимальный срок доставки - воспользоваться услугами транспортной компании.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.txt)
        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema11(QWidget):

    def __init__(self):

        button_color = Parameters.Color().whatcolor()

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Корректировки по счёту')
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.6481481481481481)

        topleft1 = QPushButton("Заказ уже производится или произведён:", self)
        topleft1.setStyleSheet("background-color: {0}".format(button_color))
        topleft1.clicked.connect(self.show_tema111)

        topleft2 = QPushButton("Заказ ещё не не передан на изготовление:", self)
        topleft2.setStyleSheet("background-color: {0}".format(button_color))
        topleft2.clicked.connect(self.show_tema112)

        hbox = QHBoxLayout()
        hbox.addWidget(topleft1)
        hbox.addWidget(topleft2)

        self.setLayout(hbox)

    def show_tema111(self):

        self.w11 = Tema111()
        self.w11.show()

    def show_tema112(self):
        self.w12 = Tema112()
        self.w12.show()


class Tema111(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Заказ производится или произведен'

        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Никаких корректировок уже быть не может. ' \
                   '\nПартнёр обязан забрать изготовленный для него товар.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema112(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()
        self.setWindowIcon(QIcon('logo.png'))
        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Заказ не передан на изготовление'
        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Возможна оперативная корретировка заказа ' \
                   '\n(с обязательным уточнением информации по срокам передачи в производство в Рыбинске).'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Ans2(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        button_color = Parameters.Color().whatcolor()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle('Вопросы по поставке продукции')

        self.setFixedSize(window_w1 * 0.625, window_h1 * 0.7407407407407407)

        topcenter1 = QPushButton("Становится известно о переносе "
                                 "\nсрока изготовления продукции в Рыбинске, "
                                 "\nза которую уже была внесена 100% предоплата партнёром.", self)
        topcenter1.setStyleSheet("background-color: {0}".format(button_color))
        topcenter1.clicked.connect(self.show_tema8)

        topcenter2 = QPushButton("Партнёр интересуется о сроках поставки товара,"
                                 "\nт.к. ранее уже была частичная отгрузка; "
                                 "\nпросит поторопить производство.", self)
        topcenter2.setStyleSheet("background-color: {0}".format(button_color))
        topcenter2.clicked.connect(self.show_tema9)

        topcenter3 = QPushButton("Партнёр просит уточнить причину задержки товара"
                                 "\nне в официальный срок (30 дней)"
                                 "\nпри условии полной или частичной предоплаты.", self)
        topcenter3.setStyleSheet("background-color: {0}".format(button_color))
        topcenter3.clicked.connect(self.show_tema10)

        topcenter4 = QPushButton("При пересчёте полученного товара на складе,"
                                 "\nпартнёр выявил факт пересорта "
                                 "\nпродукции/ошибки в товарной накладной.", self)
        topcenter4.setStyleSheet("background-color: {0}".format(button_color))
        topcenter4.clicked.connect(self.show_tema6)

        vbox = QVBoxLayout()
        vbox.addWidget(topcenter1)
        vbox.addWidget(topcenter2)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(topcenter3)
        vbox2.addWidget(topcenter4)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)

    def show_tema8(self):
        self.w21 = Tema8()
        self.w21.show()

    def show_tema9(self):
        self.w22 = Tema9()
        self.w22.show()

    def show_tema10(self):
        self.w23 = Tema10()
        self.w23.show()

    def show_tema6(self):
        self.w24 = Tema6()
        self.w24.show()


class Tema8(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.title = 'Перенос сроков изготовления'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Последовательность действий следующая:' \
                   '\n 1) Связаться с партнёром, извиниться' \
                   '\nи сообщить о переносе сроков изготовления продукции' \
                   '\n(предварительно уточнив их в Рыбинске).' \
                   '\n 2) Если это поставка срочно нужна партнёру,' \
                   '\nто попробовать отгрузить со склада в Москве' \
                   '\n(при условии наличия товара).' \
                   '\nВАЖНО! Относиться это должно только к группам товара А и В.' \
                   '\n 3) Если партнёр просит заменить часть продукции' \
                   '\n(и изготовление товара в Рыбинске ещё не началось) – ' \
                   '\nвозможно предоставление замены' \
                   '\n(только в случае крайней необходимости для партнёра).' \
                   '\nНеобходимости провести корректировку в 1С,' \
                   '\nсделав корректировку в Заказе Покупателя.'
        answer2_1 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer2_1, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):

        pyperclip.copy(self.txt)


class Tema9(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Информация о сроках поставки'
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Последовательность действий следующая:' \
                   '\n 1) Уточнить данную информацию для партнёра' \
                   '\nна производстве в Рыбинске' \
                   '\n(вовремя будет сдан товар или есть задержки).' \
                   '\n 2) Если ещё не вышел срок изготовления продукции – ' \
                   '\nсообщить через сколько будет товар.' \
                   '\n 3) Если срок изготовления продукции уже прошёл -' \
                   '\nизвиниться и сообщить о переносе сроков изготовления продукции.' \
                   '\nЕсли товар срочно нужен партнёру -' \
                   '\nто попробовать отгрузить со склада в Москве' \
                   '\n(при условии наличия товара).' \
                   '\nВНИМАНИЕ! Это относится только к продукции категории А и В. '
        answer2_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer2_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):

        pyperclip.copy(self.txt)


class Tema10(QWidget):

    def __init__(self):

        button_color = Parameters.Color().whatcolor()

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle('Информация о задержке товара')

        self.setFixedSize(window_w1 * 0.5208333333333333, window_h1 * 0.6481481481481481)

        topleft1 = QPushButton("Товар был оплачен партнёром на 100%, либо 50%/50% "
                               "\n(всё было оплачено ДО момента предполагаемой отгрузки)", self)
        topleft1.setStyleSheet("background-color: {0}".format(button_color))
        topleft1.clicked.connect(self.show_tema101)

        topleft2 = QPushButton("Товар был оплачен партнёром только на 50%", self)
        topleft2.setStyleSheet("background-color: {0}".format(button_color))
        topleft2.clicked.connect(self.show_tema102)

        hbox = QHBoxLayout()
        hbox.addWidget(topleft1)
        hbox.addWidget(topleft2)

        self.setLayout(hbox)

    def show_tema101(self):
        self.w11 = Tema101()
        self.w11.show()

    def show_tema102(self):
        self.w12 = Tema102()
        self.w12.show()


class Tema101(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.title = 'Товар оплачен на 100% или 50% (До момента предполагаемой отгрузки)'
        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Необходимо объяснить,' \
                   '\nчто была большая загруженность производства,' \
                   '\nприкладываются все усилия,' \
                   '\nчтобы ускорить выпуск партии товара партнёра.' \
                   '\nВНИМАНИЕ! Если партнёр не проблемный и всегда вовремя платит' \
                   '\n(держит свои обещания),' \
                   '\nто можно попробовать отгрузить часть продукции со склада' \
                   '\nпри его наличии – это право остаётся за КП.' \
                   '\nОтгрузить можно только продукцию группы А и В.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema102(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Товар оплачен только на 50%'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Чаще всего вторые 50% (отсрочку) не оплачивают,' \
                   '\nпока нет сообщения от КП о том,' \
                   '\nчто товар готов к отгрузке.' \
                   '\nЕсли так случилось, повторяем действия из первого пункта' \
                   '\nи напоминаем об условиях оплаты отсрочки.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema6(QWidget):

    def __init__(self):

        button_color = Parameters.Color().whatcolor()

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle('Факт пересорта/ошибки на складе')

        self.setFixedSize(window_w1 * 0.5208333333333333, window_h1 * 0.6481481481481481)

        topleft1 = QPushButton("Документы сделаны верно", self)
        topleft1.setStyleSheet("background-color: {0}".format(button_color))
        topleft1.clicked.connect(self.show_tema61)

        topleft2 = QPushButton("Ошибка в документах, но товар отгружен правильно", self)
        topleft2.setStyleSheet("background-color: {0}".format(button_color))
        topleft2.clicked.connect(self.show_tema62)

        topleft3 = QPushButton("Ошибка в документах и товар отгружен неправильно", self)
        topleft3.setStyleSheet("background-color: {0}".format(button_color))
        topleft3.clicked.connect(self.show_tema63)

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(topleft1)
        vbox.addWidget(topleft2)
        vbox.addWidget(topleft3)
        hbox.addLayout(vbox)

        self.setLayout(hbox)

    def show_tema61(self):
        self.w11 = Tema61()
        self.w11.show()

    def show_tema62(self):
        self.w12 = Tema62()
        self.w12.show()

    def show_tema63(self):
        self.w13 = Tema63()
        self.w13.show()


class Tema61(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.title = 'Документы верны'
        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Просим со следующим забором груза привезти' \
                   '\nне верно отгруженный товар в московский офис' \
                   '\nи меняем его на необходимый партнёру' \
                   '\n(строго в соответствии с ТН),' \
                   '\nесли отгрузка была со склада в Москве.' \
                   '\nЕсли отгрузка была со склада в Рыбинске,' \
                   '\nто предлагается отправить партнёру нужный товар со следующей отгрузкой,' \
                   '\nлибо оформить срочную доставку его в офис в Москве.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema62(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.title = 'Ошибка в документах'
        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Делается корректировка в Заказе Покупателю,' \
                   '\nреализации (всех задействованных документах),' \
                   '\nпосле чего готовится новый комплект документов' \
                   '\nи о них сообщается партнёру' \
                   '\n(док-ты высылаются по почте в электронном виде)' \
                   '\nс просьбой подписать и передать при первой возможности.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema63(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()
        self.setWindowIcon(QIcon('logo.png'))
        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Ошибка в документах, товар отгружен неправильно'
        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Делается корректировка в Заказе Покупателю,' \
                   '\nреализации (всех задействованных документах),' \
                   '\nпосле чего готовится новый комплект документов' \
                   '\nи о них сообщается партнёру (док-ты высылаются по почте в электронном виде).' \
                   '\nПросим со следующим забором груза привезти' \
                   '\nне верно отгруженный товар в московский офис и меняем его на необходимый партнёру' \
                   '\n(строго в соответствии с ТН), если отгрузка была со склада в Москве.' \
                   '\nЕсли отгрузка была со склада в Рыбинске,' \
                   '\nто предлагается отправить партнёру нужный товар со следующей отгрузкой,' \
                   '\nлибо оформить срочную доставку его в офис в Москве. '
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Ans3(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        button_color = Parameters.Color().whatcolor()
        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle('Вопросы по оплате')

        self.setFixedSize(window_w1 * 0.625, window_h1 * 0.7407407407407407)

        topcenter1 = QPushButton("У Партнёра есть просрочка оплаты по предыдущим счетам,"
                                 "\nон хочет продлить срок оплаты по ним"
                                 "\nс возможностью дальнейших отгрузок по новым счетам.", self)
        topcenter1.setStyleSheet("background-color: {0}".format(button_color))
        topcenter1.clicked.connect(self.show_tema1)

        topcenter2 = QPushButton("Партнёр хочет отгрузку ранее оплаченного товара,"
                                 "\nно в данный момент просрочил даты оплаты других счетов", self)
        topcenter2.setStyleSheet("background-color: {0}".format(button_color))
        topcenter2.clicked.connect(self.show_tema4)

        vbox = QVBoxLayout()
        vbox.addWidget(topcenter1)
        vbox.addWidget(topcenter2)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)

        self.setLayout(hbox)

    def show_tema1(self):
        self.w21 = Tema1()
        self.w21.show()

    def show_tema4(self):
        self.w22 = Tema4()
        self.w22.show()


class Tema1(QWidget):

    def __init__(self):

        button_color = Parameters.Color().whatcolor()

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle('Просрочка оплаты по прошлым счетам')

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.6481481481481481)

        topleft1 = QPushButton("При сумме долга более 500 000 рублей", self)
        topleft1.setStyleSheet("background-color: {0}".format(button_color))
        topleft1.clicked.connect(self.show_tema1_1)

        topleft2 = QPushButton("При сумме долга менее 500 000 рублей", self)
        topleft2.setStyleSheet("background-color: {0}".format(button_color))
        topleft2.clicked.connect(self.show_tema1_2)

        hbox = QHBoxLayout()
        hbox.addWidget(topleft1)
        hbox.addWidget(topleft2)

        self.setLayout(hbox)

    def show_tema1_1(self):

        self.w11 = TemA11()
        self.w11.show()

    def show_tema1_2(self):
        self.w12 = TemA12()
        self.w12.show()


class TemA11(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Сумма долга более 500 000 рублей'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Должна быть приостановка всех отгрузок до момента оплаты старых долгов.' \
                   '\nНа усмотрение КП (при срочной или сверх важной операции)' \
                   '\nможно предложить Партнёру 100% предоплату' \
                   '\nпо счёту с уточнением информации по срокам оплаты прошлых счетов.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class TemA12(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.setWindowIcon(QIcon('logo.png'))
        self.title = 'Сумма долга менее 500 000 рублей'
        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Партнёр может написать гарантийное письмо с точными сроками оплаты' \
                   '\n(в разумных пределах) и номерами счетов.' \
                   '\nПо новым счетам предусматривается оплата 100%.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema4(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Досрочная отгрузка'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Несмотря на то, что из-за неоплаты старых счетов партнёр' \
                   '\nможет находится в «стоп-листе», оплаченный товар должен быть передан покупателю.' \
                   '\nНо необходимо уведомить партнёра о том,' \
                   '\nчто данная отгрузка не означает отгрузку неоплаченных и новых счетов до того момента, ' \
                   '\nпока отсрочка не будет погашена.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):

        pyperclip.copy(self.txt)


class Ans4(QWidget):

    def __init__(self):
            window_w1 = Parameters.ParameterSize().ww()
            window_h1 = Parameters.ParameterSize().wh()

            button_color = Parameters.Color().whatcolor()
            super(QWidget, self).__init__()

            self.setFont(QFont('Century Gothic', 10))
            self.setWindowIcon(QIcon('logo.png'))
            self.setWindowTitle('Вопросы по подбору продукции')

            self.setFixedSize(window_w1 * 0.625, window_h1 * 0.7407407407407407)

            topcenter1 = QPushButton("Партнёр просит проконсультировать его относительно артикула продукции"
                                     "\n(например, озвучить длину штифта)"
                                     "\nи просит подобрать к нему артикулы для составления типового комплекта"
                                     "\n(Допустим комплект для операции на прокс. бедро). ", self)
            topcenter1.setStyleSheet("background-color: {0}".format(button_color))
            topcenter1.clicked.connect(self.show_tema16)

            topcenter2 = QPushButton("Партнёр хочет уточнить,"
                                     "\nподходит ли та или иная продукция для совмещения с продукцией другого бренда"
                                     "\n(Например штифты -Остеомед, а винты – Синтез).", self)
            topcenter2.setStyleSheet("background-color: {0}".format(button_color))
            topcenter2.clicked.connect(self.show_tema15)

            vbox = QVBoxLayout()
            vbox.addWidget(topcenter1)
            vbox.addWidget(topcenter2)

            hbox = QHBoxLayout()
            hbox.addLayout(vbox)

            self.setLayout(hbox)

    def show_tema16(self):
        self.w41 = Tema16()
        self.w41.show()

    def show_tema15(self):
        self.w42 = Tema15()
        self.w42.show()


class Tema15(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Совмещение с продукицей другого бренда'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Последовательность действий следующая:' \
                   '\n 1) В первую очередь необходимо уточнить,' \
                   '\nс чем связана такая ситуация, почему необходимо совмещать продукцию.' \
                   '\n 2) Уточнить ифнормацию по данной продукции у Главного Менеджера/Складовщика ' \
                   '\n(это же касается и вопросов: подходит ли чей-либо другой инструмент ' \
                   '\nи импланты к нашим имплантам и инструментам).' \
                   '\n 3) Можно сообщить, что товар более дорогих производителей (Синтез)' \
                   '\nможно использовать для прод. «Остеомед-М».' \
                   '\nВНИМАНИЕ! Единолично такую информацию лучше не предоставлять во избежание спорных ситуаций,' \
                   '\nстоит запросить письменное подтверждение опытных коллег.'
        answer3_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer3_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):

        pyperclip.copy(self.txt)


class Tema16(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Отгрузка до оплаты, имеется просрочка'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Несмотря на то, что из-за неоплаты старых счетов партнёр может находится в «стоп-листе»,' \
                   '\nоплаченный товар должен быть передан покупателю.' \
                   '\nНо необходимо уведомить партнёра о том,' \
                   '\nчто данная отгрузка не означает отгрузку неоплаченных и новых счетов до того момента,' \
                   '\nпока отсрочка не будет погашена.'
        answer3_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer3_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):

        pyperclip.copy(self.txt)


class Ans5(QWidget):

    def __init__(self):

            window_w1 = Parameters.ParameterSize().ww()
            window_h1 = Parameters.ParameterSize().wh()

            button_color = Parameters.Color().whatcolor()
            super(QWidget, self).__init__()

            self.setFont(QFont('Century Gothic', 10))
            self.setWindowIcon(QIcon('logo.png'))
            self.setWindowTitle('Вопросы по аренде инструмента')

            self.setFixedSize(window_w1 * 0.625, window_h1 * 0.7407407407407407)

            topcenter1 = QPushButton("Партнёр хочет заказать продление аренды инструмента."
                                     "\nНо при этом у него есть долги по счетам/проблемы"
                                     "\nс регулярными оплатами/иные невыполненные финансовые обязательства.", self)
            topcenter1.setStyleSheet("background-color: {0}".format(button_color))
            topcenter1.clicked.connect(self.show_tema2)

            topcenter2 = QPushButton("Срочно (день в день) нужен инструмент под операцию,"
                                     "\nно его нет на складе компании в Москве.", self)
            topcenter2.setStyleSheet("background-color: {0}".format(button_color))
            topcenter2.clicked.connect(self.show_tema5)

            topcenter3 = QPushButton("Партнёр сообщает, что с Главным Менеджером было оговорено"
                                     "\nдобавление инструмента в счёт за импланты "
                                     "\n(т.н. равномерное «размазывание» стоимости инструмента по всему счёту).", self)
            topcenter3.setStyleSheet("background-color: {0}".format(button_color))
            topcenter3.clicked.connect(self.show_tema20)

            vbox = QVBoxLayout()
            vbox.addWidget(topcenter1)
            vbox.addWidget(topcenter2)
            vbox.addWidget(topcenter3)

            hbox = QHBoxLayout()
            hbox.addLayout(vbox)

            self.setLayout(hbox)

    def show_tema2(self):
        self.w51 = Tema2()
        self.w51.show()

    def show_tema5(self):
        self.w52 = Tema5()
        self.w52.show()

    def show_tema20(self):
        self.w53 = Tema20()
        self.w53.show()


class Tema2(QWidget):

    def __init__(self):
            button_color = Parameters.Color().whatcolor()

            window_w1 = Parameters.ParameterSize().ww()
            window_h1 = Parameters.ParameterSize().wh()

            super(QWidget, self).__init__()

            self.setFont(QFont('Century Gothic', 10))
            self.setWindowTitle('Продление аренды при имеющихся долгах')
            self.setWindowIcon(QIcon('logo.png'))
            self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.6481481481481481)

            topleft1 = QPushButton("Если у партнёра имеются неиспользованные штифты для инструмента", self)
            topleft1.setStyleSheet("background-color: {0}".format(button_color))
            topleft1.clicked.connect(self.show_tema21)

            topleft2 = QPushButton("Если у партнёра не имеются неиспользованные штифты для инструмента", self)
            topleft2.setStyleSheet("background-color: {0}".format(button_color))
            topleft2.clicked.connect(self.show_tema22)

            hbox = QHBoxLayout()
            vbox = QVBoxLayout()
            vbox.addWidget(topleft1)
            vbox.addWidget(topleft2)
            hbox.addLayout(vbox)
            self.setLayout(hbox)

    def show_tema21(self):
            self.w11 = Tema21()
            self.w11.show()

    def show_tema22(self):
            self.w12 = Tema22()
            self.w12.show()


class Tema21(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Есть неиспользованные штифты'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Если Партнёр обладает неиспользованными штифтами,' \
                   '\nто продление инструмента можно согласовать. ' \
                   '\nВместе с этим необходимо запросить ГП' \
                   '\nоб оплате долгов/выполнении просроченных финансовых обязательств.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema22(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Нет неиспользованных штифтов'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Если Партнёр не обладает неиспользованными штифтами,' \
                   '\nто в продлении инструмента необходимо отказать.' \
                   '\nИсключение - отдельный запрос важной для нас больницы.'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):
        pyperclip.copy(self.txt)


class Tema5(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Срочно нужен инструмент, но его нет на складе'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Последовательность действий следующая:' \
                   '\n 1) Уточнить в каких больницах/у каких дилеров Москвы' \
                   '\nнаходится необходимый инструмент' \
                   '\n(поиск ведётся по дилерам и больницам с помощью информации из 1С).' \
                   '\n 2) Попробовать согласовать его передачу на 1 срочную операцию.' \
                   '\n 3) В случае, если свободного инструмента нет,' \
                   '\nпопробовать подыскать аналог инструмента Синтеза и т.д.' \
                   '\n 4) Если нет абсолютно никаких вариантов -' \
                   '\nто необходимо сообщить об этом партнёру и предложить перенести операцию.' \
                   '\nВыяснить и сообщить партнёру, когда инструмент будет на складе в Москве.'
        answer5_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer5_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):

        pyperclip.copy(self.txt)


class Tema20(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Добавление инструмента оговорено'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Последовательность действий следующая:' \
                   '\n 1) Необходимо написать письмо партнёру (Главного Менеджера в копию)' \
                   '\nпо уточнению счёта на импланты' \
                   '\n(согласовать необходимое кол-во, артикулы) и комплектацию предполагаемого инструмента' \
                   '\n(комплектация выбирается КП из Ф/З и указывается в письме).' \
                   '\n 2) После этого ожидается согласование итогового счёта с партнёром,' \
                   '\nв котором уже сделана наценка за инструмент.' \
                   '\n 3) После согласования и оплаты – счёт отправляется на производство,' \
                   '\nсписок необходимого инструмента в формате Excel пересылается по почте в Рыбинск' \
                   '\n(используется документ внутреннего заказа).'
        answer5_3 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer5_3, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):

        pyperclip.copy(self.txt)


class Ans6(QWidget):

    def __init__(self):

            window_w1 = Parameters.ParameterSize().ww()
            window_h1 = Parameters.ParameterSize().wh()

            button_color = Parameters.Color().whatcolor()
            super(QWidget, self).__init__()

            self.setFont(QFont('Century Gothic', 10))
            self.setWindowIcon(QIcon('logo.png'))
            self.setWindowTitle('Прочие вопросы')

            self.setFixedSize(window_w1 * 0.625, window_h1 * 0.7407407407407407)

            topcenter1 = QPushButton("Партнёр просит уточнить, можно ли делать МРТ,"
                                     "\nхочет сертификат на разрешение МРТ исследования.", self)
            topcenter1.setStyleSheet("background-color: {0}".format(button_color))
            topcenter1.clicked.connect(self.show_tema3)

            topcenter2 = QPushButton("Партнёр убеждает о сторонних устных договорённостях с Главным Менеджером,"
                                     "\nдающих ему некоторое преимущество в спорных ситуациях"
                                     "\n(аренда/срочная отгрузка/другое).", self)
            topcenter2.setStyleSheet("background-color: {0}".format(button_color))
            topcenter2.clicked.connect(self.show_tema7)

            topcenter3 = QPushButton("Партнёр просит сообщить реальное наличие товара на складе для срочной операции"
                                     "\n(файл наличия на складах ему ранее с утра отправлялся),"
                                     "\nу него есть подозрения относительно актуальности информации.", self)
            topcenter3.setStyleSheet("background-color: {0}".format(button_color))
            topcenter3.clicked.connect(self.show_tema19)

            vbox = QVBoxLayout()
            vbox.addWidget(topcenter1)
            vbox.addWidget(topcenter2)
            vbox.addWidget(topcenter3)

            hbox = QHBoxLayout()
            hbox.addLayout(vbox)

            self.setLayout(hbox)

    def show_tema3(self):
        self.w61 = Tema3()
        self.w61.show()

    def show_tema7(self):
        self.w62 = Tema7()
        self.w62.show()

    def show_tema19(self):
        self.w63 = Tema19()
        self.w63.show()


class Tema3(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'МРТ'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Необходимо предоставить Партнёру подобный сертификат,' \
                   '\nкоторый был составлен и выслан КП в 2018 г.' \
                   '\nВ нём содержится подробная информация о том,' \
                   '\nчто с имплантатами ООО "ОСТЕОМЕД-М" можно проводить МРТ.'
        answer6_1 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer6_1, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)
    def copy(self):

        pyperclip.copy(self.txt)


class Tema7(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Есть договоренность'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Последовательность действий следующая' \
                   '\n 1) Узнать у Главного Менеджера, правда ли это. ' \
                   'Написать, позвонить, другим способом связаться с ним,' \
                   '\nпостараться выяснить о чём именно была договорённость.' \
                   '\n 2) В случае, если Главный Менеджер недоступен,' \
                   '\nпопросить партнёра предоставить письменное подтверждение' \
                   '\nмежду руководителями о данной договоренности' \
                   '\n(что бы иметь на руках какое-то подтверждение для руководства при запросе обоснования действий).'
        answer6_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer6_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):

        pyperclip.copy(self.txt)


class Tema19(QWidget):

    def __init__(self):

        window_w1 = Parameters.ParameterSize().ww()
        window_h1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setWindowIcon(QIcon('logo.png'))
        self.setFont(QFont('Century Gothic', 10))
        self.title = 'Реальное наличие товара'
        self.setWindowTitle(self.title)

        self.setFixedSize(window_w1 * 0.46875, window_h1 * 0.4259259259259259)

        self.txt = 'Последовательность действий следующая:' \
                   '\n 1) Если это небольшой кол-во продукции – можно проверить наличие на складе в Москве.' \
                   '\n 2) Если это большое кол-во продукции (от 7-10 поз.) – говорим,' \
                   '\nчто информация актуальна и верна, что необходимо пользоваться ею для заказа.'
        answer6_3 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)
        copy_button = CopyButton.button(self)
        copy_button.clicked.connect(self.copy)

        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(answer6_3, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open("Text.txt", "w", encoding='windows-1251') as textfile:
            textfile.write(self.txt)

        with open("Title.txt", "w", encoding='windows-1251') as textfile:

            textfile.write(self.title)

    def copy(self):

        pyperclip.copy(self.txt)
