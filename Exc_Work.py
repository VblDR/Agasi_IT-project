from openpyxl import Workbook, load_workbook
from PyQt5.QtWidgets import QMessageBox


def pusk_but_click(articul, number, check):

    if (len(articul) == 3 or len(articul) == 7 or len(articul) == 6) and number != '':

        if check == 0:
            if len(articul) == 7:
                art = articul[0:3]
            elif len(articul) == 12:
                art = articul[]
            what_name(art, int(number))
        elif check == 1:
            numlist, namlist, artlist = what_name2(articul, int(number))
            return numlist, namlist, artlist
    else:
        warning2 = QMessageBox()
        warning2.setIcon(QMessageBox.Critical)
        warning2.setText("Возникла ошибка. "
                         "\nВы не заполнили поля 'Атикул' или 'Количество' или заполнили их неправильно.")
        warning2.setWindowTitle("Ошибка")
        warning2.setStandardButtons(QMessageBox.Cancel)

        rs = warning2.exec()
        return rs



# эндопротезы
def what_name(articul, number):
    return 0


# изделия
def what_name2(art, number):

    exbook = load_workbook('exwork.xlsx', data_only=True)
    page = exbook.active
    indlist = []
    for i in range(2, 1973):
        articul2 = page.cell(row=i, column=1).value
        if articul2[0: 3] == art:

            indlist.append(i)

    namlist = []
    percentlist = []
    artlist = []
    for i in indlist:
        namlist.append(page.cell(row=i, column=2).value)
        percentlist.append(round(page.cell(row=i, column=10).value, 2))
        artlist.append(page.cell(row=i, column=1).value)
    numlist = []
    for i in percentlist:
        numlist.append(round(i*number))

    if sum(numlist) != number:
        number2 = number - sum(numlist)
        for i in range(number2):
            ind = numlist.index(min(numlist))
            numlist[ind] += 1

    if sum(numlist) >= number:
        number2 = sum(numlist) - number
        for i in range(number2):
            numlist[percentlist.index(min(percentlist))] -= 1
            percentlist[percentlist.index(min(percentlist))] = 9999

    return numlist, namlist, artlist


def create(row, filename):

    wb = Workbook()
    ws = wb.active
    ws.title = 'Предложение'

    for i in row:
        ws.append(i)


    wb.save(filename)

    welldone = QMessageBox()
    welldone.setIcon(QMessageBox.Information)
    welldone.setText("Сохранение прошло успешно.")
    welldone.setWindowTitle("Выполнено!")
    welldone.setStandardButtons(QMessageBox.Ok)

    rslt = welldone.exec()

    return rslt
