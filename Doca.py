import datetime
from docxtpl import DocxTemplate


# этот модуль отвечает за наполнение шаблонного договора.
def doce(company, dir_dol, fam12, filname, inn, kpp, adr, tel, email, r_s, k_s, bank, bik, dirfio2):
    # считываем нынешние дату и время
    now = datetime.datetime.today()
    date = now.strftime("«%d» %B %Y")
    # открываем шаблонный договор, в котором уже проставлены метки
    doca = DocxTemplate("раз договор 2.docx")
    # словарь замен меток на введенные пользователем данные
    context = {'date': date, 'comp': company, 'dirdol': dir_dol, 'dirfio': fam12, 'inn' : inn, 'kpp' : kpp,
               'adr' : adr, 'tel' : tel, 'email' : email, 'r_s' : r_s, 'k_s' : k_s, 'bank' : bank,
               'bik' : bik, 'dirdol2' : dir_dol, 'dirfio2' : dirfio2}
    # замена
    doca.render(context)
    # сохранение нового документа по указанному пути
    doca.save(filname)

    return 0
