import datetime
from docxtpl import DocxTemplate


def doce(company, dir_dol, fam12, filname, inn, kpp, adr, tel, email, r_s, k_s, bank, bik, dirfio2):
    now = datetime.datetime.today()
    date = now.strftime("«%d» %B %Y")
    doca = DocxTemplate("раз договор 2.docx")
    context = {'date': date, 'comp': company, 'dirdol': dir_dol, 'dirfio': fam12, 'inn' : inn, 'kpp' : kpp,
               'adr' : adr, 'tel' : tel, 'email' : email, 'r_s' : r_s, 'k_s' : k_s, 'bank' : bank,
               'bik' : bik, 'dirdol2' : dir_dol, 'dirfio2' : dirfio2}
    doca.render(context)
    doca.save(filname)

    return 0
