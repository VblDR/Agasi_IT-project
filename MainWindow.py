#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""

Итак, это модуль главного окна.
Навигация по модулям:
 1. Шаблонные ответы - Answers.py (основное окно), Answers1.py (окна подразделов и самих ответов)
 2. Шаблоны - Shblon.py (здесь находятся и шаблон договора, и шаблоны коммерческих предложений)
 3. Наилучшее предложение - BestOffer.py
 4. Статистика - Statistics.py
 5. Отправка пиьсма - SendEmail.py
 6. Заполнение договора - Doca.py
 7. Пользовательские параметры - Parameters.py
 8. Настройки - Settings.py
 9. Информация о приложении - Information.py
 10. Работа с данными из Excel - Exc_Work.py

Для чего:
 1. Шаблоныые ответы просто предоставляет стандартные ответы на часто встречающиеся вопросы. Это может пригодиться
  сотрудникам, если им необходимо освежить в памяти шаги решения стандартных проблем или отправить быстрый ответ
  на почту партнера.
 2. Шаблонный договор нужен для быстрого заполнения договора реквизитами.
  Шаблонное коммерческое предложение нужно для быстрой отправки предложения на почту партнера или клиента.
 3. Наилучшее предложение нужно для коммерческих представителей. Представим ситиуацию, что с вами связывается партнер,
  хочет купить определенное количество продукции определенного арткула и просит проконсультировать его.
    Так как у каждой продукции есть свои подразмеры и их продаваемость постоянно варьируется,
  то коммерческий представитель просто может узнать необходимое для закупки количество каждого подразмера
  определенного артикула, просто введа в программу артикул и общее количество для закупки.
  определенного артикула, просто введа в программу артикул и общее количество для закупки.
 4. Статистика необходима для предоставления быстрого отчета по продажам определенного продукта за определенный период
  времени. Статистика может пригодиться для прведения анализа продаваемости того или иного продукта,
  на основании которого будут сделаны выводы.

"""

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


# Главное окно программы
class MainWindow(QMainWindow):

    def __init__(self):

        super(QMainWindow, self).__init__()

        # Настройки интерфейса программы
        self.setFont(QFont('Century Gothic', 15))
        self.setWindowTitle("Книга бизнес-процессов")
        self.setWindowIcon(QIcon('logo.png'))
        self.windowW = Parameters.ParameterSize().ww()
        self.windowH = Parameters.ParameterSize().wh()
        self.setFixedSize(self.windowW * 0.6770833333333333, self.windowH * 0.8333333333333333)

        # Вкладки
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

        # Меню программы
        menubar = self.menuBar()

        setting_action = QAction(QIcon('setting.png'), '&Настройки', self)
        setting_action.setStatusTip('Открыть настройки')
        setting_action.triggered.connect(self.show_setting)
        setting_action.setShortcut('Ctrl+N')

        info_action = QAction(QIcon('info.png'), '&Информация', self)
        info_action.setStatusTip('Информация о программе')
        info_action.triggered.connect(self.show_info)
        info_action.setShortcut('Ctrl+I')

        exit_action = QAction(QIcon('quit.png'), '&Выход', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Выход из программы')
        exit_action.triggered.connect(qApp.quit)

        program_menu = menubar.addMenu('&Программа')
        program_menu.addAction(setting_action)
        program_menu.addAction(info_action)
        program_menu.addAction(exit_action)

    # вызов окна информации
    def show_info(self):

        self.info = Information.Info()
        self.info.show()

    # вызов окна настроек
    def show_setting(self):

        self.setting = Settings.Setting()
        self.setting.show()


# Запуск программы
if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = MainWindow()
        ex.show()
        sys.exit(app.exec_())
