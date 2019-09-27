#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Parameters as Parameters
import Settings as Settings
import Information as Information
import Answers as Answers
import Shablon as Shablon
import BestOffer as BestOffer
import Statistics as Statistics


class MainWindow(QMainWindow):

    def __init__(self):

        super(QMainWindow, self).__init__()

        self.setFont(QFont('Century Gothic', 15))
        self.setWindowTitle("Книга бизнес-процессов")

        self.setWindowIcon(QIcon('logo.png'))
        self.windowW = Parameters.ParameterSize().ww()
        self.windowH = Parameters.ParameterSize().wh()

        self.setFixedSize(self.windowW * 0.6770833333333333, self.windowH * 0.8333333333333333)

        ans = Answers.FormWidget(self)
        shablon = Shablon.FormWidget1(self)
        best_offer = BestOffer.FormWidget2(self)
        statistics = Statistics.FormWidget3(self)

        tab = QTabWidget()
        tab.addTab(ans, "Ответы")
        tab.addTab(shablon, "Шаблоны")
        tab.addTab(best_offer, "Наилучшее предложение")
        tab.addTab(statistics, "Статистика")

        main_widget = QWidget()
        vbox = QHBoxLayout()
        vbox.addWidget(tab)
        main_widget.setLayout(vbox)
        self.setCentralWidget(main_widget)

        # MenuBar

        menubar = self.menuBar()

        settingAction = QAction(QIcon('setting.png'), '&Настройки', self)
        settingAction.setStatusTip('Открыть настройки')
        settingAction.triggered.connect(self.show_setting)
        settingAction.setShortcut('Ctrl+N')

        infoAction = QAction(QIcon('info.png'), '&Информация', self)
        infoAction.setStatusTip('Информация о программе')
        infoAction.triggered.connect(self.show_info)
        infoAction.setShortcut('Ctrl+I')

        exitAction = QAction(QIcon('quit.png'), '&Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выход из программы')
        exitAction.triggered.connect(qApp.quit)

        programMenu = menubar.addMenu('&Программа')
        programMenu.addAction(settingAction)
        programMenu.addAction(infoAction)
        programMenu.addAction(exitAction)

    def show_info(self):

        self.info = Information.Info()
        self.info.show()

    def show_setting(self):

        self.setting = Settings.Setting()
        self.setting.show()


if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = MainWindow()
        ex.show()
        sys.exit(app.exec_())
