#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Parameters as Parameters
import Answers1 as ProgramBody


# Основное окно шаблонных ответов
class FormWidget(QWidget):

    def __init__(self, parent):

        super(FormWidget, self).__init__(parent)

        self.setFont(QFont('Century Gothic', 15))
        self.button_color = Parameters.Color().whatcolor()
        self.setWindowIcon(QIcon('logo.png'))
        vbox = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        hbox = QHBoxLayout()

        # Далее идут разделы, по которым распределяются ответы
        topleft = QPushButton("Вопросы по заказу продукции", self)
        topleft.setStyleSheet("background-color: {0}".format(self.button_color))
        topleft.clicked.connect(self.show_tema1)

        topcenter = QPushButton("Вопросы по поставке продукции", self)
        topcenter.setStyleSheet("background-color: {0}".format(self.button_color))
        topcenter.clicked.connect(self.show_tema2)

        topright = QPushButton("Вопросы по оплате продукции", self)
        topright.setStyleSheet("background-color: {0}".format(self.button_color))
        topright.clicked.connect(self.show_tema3)

        bottomleft = QPushButton("Вопросы по подбору продукции", self)
        bottomleft.setStyleSheet("background-color: {0}".format(self.button_color))
        bottomleft.clicked.connect(self.show_tema4)

        bottomcenter = QPushButton("Вопросы по аренде инструмента", self)
        bottomcenter.setStyleSheet("background-color: {0}".format(self.button_color))
        bottomcenter.clicked.connect(self.show_tema5)

        bottomright = QPushButton("Прочие вопросы", self)
        bottomright.setStyleSheet("background-color: {0}".format(self.button_color))
        bottomright.clicked.connect(self.show_tema6)

        # Компоновка разделов в окне
        vbox.addWidget(topleft, stretch=10)
        vbox.addWidget(bottomleft, stretch=10)

        vbox2.addWidget(topcenter, stretch=10)
        vbox2.addWidget(bottomcenter, stretch=10)

        vbox3.addWidget(topright, stretch=10)
        vbox3.addWidget(bottomright, stretch=10)

        hbox.addLayout(vbox)
        hbox.addLayout(vbox2)
        hbox.addLayout(vbox3)

        self.setLayout(hbox)


# Вызов окон разделов
    def show_tema1(self):
        self.w1 = ProgramBody.Ans1()
        self.w1.show()

    def show_tema2(self):
        self.w2 = ProgramBody.Ans2()
        self.w2.show()

    def show_tema3(self):
        self.w3 = ProgramBody.Ans3()
        self.w3.show()

    def show_tema4(self):
        self.w4 = ProgramBody.Ans4()
        self.w4.show()

    def show_tema5(self):
        self.w5 = ProgramBody.Ans5()
        self.w5.show()

    def show_tema6(self):
        self.w6 = ProgramBody.Ans6()
        self.w6.show()
