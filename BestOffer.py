from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import Exc_Work as Exc
import Parameters as Parameters


class FormWidget2(QWidget):

    def __init__(self, parent):

        super(FormWidget2, self).__init__(parent)

        self.setFont(QFont('Century Gothic', 15))
        self.setWindowIcon(QIcon('logo.png'))
        window_w = Parameters.ParameterSize().ww()

        # выбор типа изделий
        self.endop = QRadioButton("Эндопротезы")
        self.izd = QRadioButton("Изделия")

        # данные с артикулами изделий в зависимости от типа
        self.button_by_data = {
            self.endop: 'endo_art.txt',
            self.izd: 'izd_art.txt'
        }

        # группируем компоненты в окне
        self.hbox = QButtonGroup()
        self.hbox.addButton(self.endop)
        self.hbox.addButton(self.izd)
        self.hbox.buttonClicked.connect(self._on_radio_button_click)
        box = QHBoxLayout()
        box.addWidget(self.endop)
        box.addWidget(self.izd)

        # ввод артикула и количества для закупки
        self.art_line = QLineEdit()
        self.art_line.setPlaceholderText('Введите артикул')

        self.art_line_comp = ['']

        # автозаполнение поля для ввода артикула
        self.completer = QCompleter(self.art_line_comp, self.art_line)
        self.art_line.setCompleter(self.completer)

        # количество изделий, требуемых для закупки
        self.num_line = QLineEdit()
        self.num_line.setPlaceholderText("Введите количество")

        # кнопка рассчета изделий и количества
        pusk = QPushButton("Поиск")
        pusk.clicked.connect(self.pusk_click)

        # кнопка создания документа
        cr_but = QPushButton('Экспорт')
        cr_but.clicked.connect(self.create_doc)

        # кнопка очистки таблицы
        clear_but = QPushButton('Очистить')
        clear_but.clicked.connect(self.clear_tab)

        # таблица вывода информации
        self.tab = QTableWidget()
        self.tab.setColumnCount(3)
        self.tab.setHorizontalHeaderLabels(['Артикул', 'Наименоване', 'Количество'])
        self.tab.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.tab.horizontalHeaderItem(1).setTextAlignment(Qt.AlignCenter)
        self.tab.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        self.tab.setColumnWidth(0, window_w*0.17)
        self.tab.setColumnWidth(1, window_w*0.362)
        self.tab.setColumnWidth(2, window_w*0.11)
        self.tab.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tab.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # группируем компоненты в окне
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.art_line)
        hbox1.addWidget(self.num_line)
        hbox1.addWidget(pusk)

        # группируем компоненты в окне
        hbox2 = QHBoxLayout()
        hbox2.addWidget(clear_but)
        hbox2.addWidget(cr_but)

        # группируем компоненты в окне
        vbox = QVBoxLayout()
        vbox.addLayout(box)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.tab)
        vbox.addLayout(hbox2)

        # основное поле
        self.setLayout(vbox)

    # изменение данных с изделиями в зависимости от выбранного типа изделия
    def _on_radio_button_click(self, button):
        way = self.button_by_data[button]

        # читаем документ, в котором хранятся номера артикулов
        with open(way, 'r') as f:
            self.art_line_comp = [p.strip() for p in f]

        # добавляем в автозаполнение артикулы
        self.completer = QCompleter(self.art_line_comp, self.art_line)
        self.art_line.setCompleter(self.completer)

    def pusk_click(self):

        art = self.art_line.text()
        num = self.num_line.text()

        # поиск данных в Excel-таблице для изделий
        if self.endop.isChecked():
            try:
                numlist, namlist, artlist = Exc.pusk_but_click(art, num, 0)
            except:
                self.clear_tab()

        # поиск данных в Excel-таблице для эндопротезов
        elif self.izd.isChecked():
            try:
                numlist, namlist, artlist = Exc.pusk_but_click(art, num, 1)
            except:
                self.clear_tab()

        # в случае ошибки
        else:

            warning = QMessageBox()
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Возникла ошибка поиска. Выберите один из типов продукции.")
            warning.setWindowTitle("Ошибка")
            warning.setStandardButtons(QMessageBox.Cancel)

            rslt = warning.exec()
            return rslt

        # заполняем таблицу артикулами продукции
        for i in range(len(artlist)):
            self.tab.setRowCount(i+1)
            item = QTableWidgetItem(artlist[i])
            item.setTextAlignment(Qt.AlignLeft)
            self.tab.setItem(i, 0, item)

        # заполняем таблицу названиями продукции
        for i in range(len(namlist)):
            item = QTableWidgetItem(namlist[i])
            item.setTextAlignment(Qt.AlignCenter)
            self.tab.setItem(i, 1, item)

        # заполняем таблицу рекомендуемым для закупки количеством продукции
        for i in range(len(numlist)):
            item = QTableWidgetItem(str(numlist[i]))
            item.setTextAlignment(Qt.AlignRight)
            self.tab.setItem(i, 2, item)

    # очистка таблицы
    def clear_tab(self):

        self.tab.setRowCount(0)

    # создание Excel-документа с данными из таблицы в главном окне
    def create_doc(self):

        if self.tab.item(0, 0) is not None:

            # окна выбора пути и имени расположения файла
            way = QFileDialog.getSaveFileName(parent=None, caption="Сохранить конфигурацию товаров",
                                              filter="Документ Excel (*.xlsx)")
            filename = way[0]

        # в случае ошибки
        else:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Возникла ошибка создания. \nНеобходимо выполнить поиск данных.")
            warning.setWindowTitle("Ошибка")
            warning.setStandardButtons(QMessageBox.Cancel)

            rslt = warning.exec()

            return rslt

        artlist = []
        namlist = []
        numlist = []

        # считываем данные из таблицы на главном экране
        for i in range(self.tab.rowCount()):
            artlist.append(self.tab.item(i, 0).text())
            namlist.append(self.tab.item(i, 1).text())
            numlist.append(self.tab.item(i, 2).text())

        # заполняем созданный Excel-документ
        row = [['Артикул', 'Наименование', 'Количество']]
        for i in range(len(numlist)):
            lst = [artlist[i], namlist[i], numlist[i]]
            row.append(lst)

        # функция создания документа в отельном модуле Exc_Work.py
        Exc.create(row, filename, 'Предложение')


