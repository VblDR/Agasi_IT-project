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

        windowW = Parameters.ParameterSize().ww()

        # выбор типа изделий
        self.endop = QRadioButton("Эндопротезы")
        self.izd = QRadioButton("Изделия")

        hbox = QHBoxLayout()
        hbox.addWidget(self.endop, alignment=Qt.AlignLeft)
        hbox.addWidget(self.izd, alignment=Qt.AlignRight)
        box = QGroupBox()
        box.setLayout(hbox)

        # ввод артикула и количества для закупки
        self.art_line = QLineEdit()
        self.art_line.setPlaceholderText('Введите артикул')

        with open('art.txt', 'r') as f:
            art_line = [p.strip() for p in f]

        completer = QCompleter(art_line, self.art_line)
        self.art_line.setCompleter(completer)

        self.num_line = QLineEdit()
        self.num_line.setPlaceholderText("Введите количество")

        # кнопка рассчета изделий и количества
        pusk = QPushButton("Поиск")
        pusk.clicked.connect(self.puskClick)

        # кнопка создания документа
        cr_but = QPushButton('Экспорт')
        cr_but.clicked.connect(self.createDoc)

        # кнопка очистки таблицы
        clear_but = QPushButton('Очистить')
        clear_but.clicked.connect(self.clearTab)

        # таблица вывода информации
        self.tab = QTableWidget()
        self.tab.setColumnCount(3)
        self.tab.setHorizontalHeaderLabels(['Артикул', 'Наименоване', 'Количество'])
        self.tab.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.tab.horizontalHeaderItem(1).setTextAlignment(Qt.AlignCenter)
        self.tab.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        self.tab.setColumnWidth(0, windowW*0.17)
        self.tab.setColumnWidth(1, windowW*0.362)
        self.tab.setColumnWidth(2, windowW*0.11)
        self.tab.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tab.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.art_line)
        hbox1.addWidget(self.num_line)
        hbox1.addWidget(pusk)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(clear_but)
        hbox2.addWidget(cr_but)

        vbox = QVBoxLayout()
        vbox.addWidget(box)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.tab)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

    def puskClick(self):

        art = self.art_line.text()
        num = self.num_line.text()

        if self.endop.isChecked():
            try:
                numlist, namlist, artlist = Exc.pusk_but_click(art, num, 0)
            except:
                print(art)
                self.clearTab()
                return 1

        elif self.izd.isChecked():

            numlist, namlist, artlist = Exc.pusk_but_click(art, num, 1)


        else:

            warning = QMessageBox()
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Возникла ошибка поиска. Выберите один из типов продукции.")
            warning.setWindowTitle("Ошибка")
            warning.setStandardButtons(QMessageBox.Cancel)

            rslt = warning.exec()
            return rslt

        for i in range(len(artlist)):
            self.tab.setRowCount(i+1)
            item = QTableWidgetItem(artlist[i])
            item.setTextAlignment(Qt.AlignLeft)
            self.tab.setItem(i, 0, item)

        for i in range(len(namlist)):
            item = QTableWidgetItem(namlist[i])
            item.setTextAlignment(Qt.AlignCenter)
            self.tab.setItem(i, 1, item)

        for i in range(len(numlist)):
            item = QTableWidgetItem(str(numlist[i]))
            item.setTextAlignment(Qt.AlignRight)
            self.tab.setItem(i, 2, item)


    def clearTab(self):

        self.tab.setRowCount(0)

    def createDoc(self):

        if self.tab.item(0, 0) is not None:

            # окна выбора пути и имени расположения файла
            way = QFileDialog.getSaveFileName(parent=None, caption="Сохранить конфигурацию товаров",
                                              filter="Документ Excel (*.xlsx)")
            filename = way[0]

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

        for i in range(self.tab.rowCount()):
            artlist.append(self.tab.item(i, 0).text())
            namlist.append(self.tab.item(i, 1).text())
            numlist.append(self.tab.item(i, 2).text())

        row = [['Артикул', 'Наименование', 'Количество']]
        for i in range(len(numlist)):
            list = [artlist[i], namlist[i], numlist[i]]
            row.append(list)

        Exc.create(row, filename)


