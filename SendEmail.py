#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QMessageBox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import email.mime.application


# модуль отправки писем

# функция отправки письма
def send_letter(uremail, urpassword, address):

    # читаем из ранее созданного файла тексты для отправки
    with open("Text.txt", "r", encoding='windows-1251') as textfile:
        m = textfile.read()

    with open("Title.txt", "r", encoding='windows-1251') as titlefile:
        title = titlefile.readline()

    # наполнение письма
    russian = 'windows-1251'
    msg = MIMEMultipart()
    msg["Subject"] = Header(title, russian)
    msg["From"] = Header(uremail)
    msg["To"] = Header(address)

    text = MIMEText(m.encode('cp1251'), 'plain', russian)
    msg.attach(text)

    check = uremail.find("@")

    '''
    Далее идут танцы с бубном и доменными именами. Они идентичны за исключением портов, доменов и сервисов, 
    которые обслуживают ту или иную почту. Для экономии времени советую посмотреть только один пример, приведенный ниже
    '''

    # если имеем дело с доменом яндекса
    if uremail[check+1:] == "yandex.ru":
        # подключаемся к серверам яндекса
        mail_lib = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        mail_lib.ehlo()

        try:
            # авторизуемся
            mail_lib.login(uremail[:check], urpassword)
            mail_lib.auth_plain()
            # отправляем письмо
            mail_lib.sendmail(uremail, address, msg.as_string())

            # выходим из почты
            mail_lib.quit()

            # окно, оповещающее об успешной отправке
            welldone = QMessageBox()
            welldone.setIcon(QMessageBox.Information)
            welldone.setText("Отправка прошла успешно.")
            welldone.setWindowTitle("Выполнено!")
            welldone.setStandardButtons(QMessageBox.Ok)

            rslt = welldone.exec()

        except:

            # окно, оповещающее о неудачной отправке
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Возникла ошибка отправки. \nПроверьте правильность введенных вами данных.")
            warning.setWindowTitle("Ошибка")
            warning.setStandardButtons(QMessageBox.Cancel)

            rslt = warning.exec()

        return rslt

    elif uremail[check+1:] == "osteomed.ru":

        mail_lib = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        mail_lib.ehlo()

        try:

            mail_lib.login(uremail, urpassword)
            mail_lib.auth_plain()
            mail_lib.sendmail(uremail, address, msg.as_string())

            mail_lib.quit()

            welldone = QMessageBox()
            welldone.setIcon(QMessageBox.Information)
            welldone.setText("Отправка прошла успешно.")
            welldone.setWindowTitle("Выполнено!")
            welldone.setStandardButtons(QMessageBox.Ok)

            rslt = welldone.exec()

        except:

            warning = QMessageBox()
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Возникла ошибка отправки. \nПроверьте правильность введенных вами данных.")
            warning.setWindowTitle("Ошибка")
            warning.setStandardButtons(QMessageBox.Cancel)

            rslt = warning.exec()

        return rslt

    else:
        mail_lib = smtplib.SMTP_SSL('smtp.mail.ru: 465')
        mail_lib.ehlo()

        try:

            mail_lib.login(uremail, urpassword)
            mail_lib.sendmail(uremail, address, msg.as_string())

            mail_lib.quit()

            welldone = QMessageBox()
            welldone.setIcon(QMessageBox.Information)
            welldone.setText("Отправка прошла успешно.")
            welldone.setWindowTitle("Выполнено!")
            welldone.setStandardButtons(QMessageBox.Ok)

            rslt = welldone.exec()

        except:

            warning = QMessageBox()
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Возникла ошибка отправки. \nПроверьте правильность введенных вами данных.")
            warning.setWindowTitle("Ошибка")
            warning.setStandardButtons(QMessageBox.Cancel)

            rslt = warning.exec()

        return rslt


# отправка коммерческого предложения, все абсолютно так же, как и с обычным письмом, но добавляется документ формата PDF
def send_kom(link, uremail, urpassword, address):
    russian = 'windows-1251'

    title = 'Коммерческое предложение. Остеомед'
    msg = MIMEMultipart()
    msg["Subject"] = Header(title, russian)
    msg["From"] = Header(uremail)
    msg["To"] = Header(address)

    fp = open(link, 'rb')
    att = email.mime.application.MIMEApplication(fp.read(), _subtype="pdf")
    fp.close()
    att.add_header('Content-Disposition', 'attachment', filename='Коммерческое предложение')
    msg.attach(att)

    check = uremail.find("@")

    if uremail[check + 1:] == "yandex.ru":
        mail_lib = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        mail_lib.ehlo()

        try:
            mail_lib.login(uremail[:check], urpassword)
            mail_lib.auth_plain()
            mail_lib.sendmail(uremail, address, msg.as_string())

            mail_lib.quit()

            welldone = QMessageBox()
            welldone.setIcon(QMessageBox.Information)
            welldone.setText("Отправка прошла успешно.")
            welldone.setWindowTitle("Выполнено!")
            welldone.setStandardButtons(QMessageBox.Ok)

            rslt = welldone.exec()

        except:

            warning = QMessageBox()
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Возникла ошибка отправки. \nПроверьте правильность введенных вами данных.")
            warning.setWindowTitle("Ошибка")
            warning.setStandardButtons(QMessageBox.Cancel)

            rslt = warning.exec()

        return rslt

    elif uremail[check + 1:] == "osteomed.ru":

        mail_lib = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        mail_lib.ehlo()

        try:

            mail_lib.login(uremail, urpassword)
            mail_lib.auth_plain()
            mail_lib.sendmail(uremail, address, msg.as_string())

            mail_lib.quit()

            welldone = QMessageBox()
            welldone.setIcon(QMessageBox.Information)
            welldone.setText("Отправка прошла успешно.")
            welldone.setWindowTitle("Выполнено!")
            welldone.setStandardButtons(QMessageBox.Ok)

            rslt = welldone.exec()

        except:

            warning = QMessageBox()
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Возникла ошибка отправки. \nПроверьте правильность введенных вами данных.")
            warning.setWindowTitle("Ошибка")
            warning.setStandardButtons(QMessageBox.Cancel)

            rslt = warning.exec()

        return rslt

    else:
        mail_lib = smtplib.SMTP_SSL('smtp.mail.ru: 465')
        mail_lib.ehlo()

        try:

            mail_lib.login(uremail, urpassword)
            mail_lib.sendmail(uremail, address, msg.as_string())

            mail_lib.quit()

            welldone = QMessageBox()
            welldone.setIcon(QMessageBox.Information)
            welldone.setText("Отправка прошла успешно.")
            welldone.setWindowTitle("Выполнено!")
            welldone.setStandardButtons(QMessageBox.Ok)

            rslt = welldone.exec()

        except:

            warning = QMessageBox()
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Возникла ошибка отправки. \nПроверьте правильность введенных вами данных.")
            warning.setWindowTitle("Ошибка")
            warning.setStandardButtons(QMessageBox.Cancel)

            rslt = warning.exec()

        return rslt