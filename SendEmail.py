#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QMessageBox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_letter(uremail, urpassword, address):

    with open("Text.txt", "r", encoding='windows-1251') as textfile:
        m = textfile.read()

    with open("Title.txt", "r", encoding='windows-1251') as titlefile:
        title = titlefile.readline()

    russian = 'windows-1251'

    msg = MIMEMultipart()
    msg["Subject"] = Header(title, russian)
    msg["From"] = Header(uremail)
    msg["To"] = Header(address)

    text = MIMEText(m.encode('cp1251'), 'plain', russian)
    msg.attach(text)

    check = uremail.find("@")

    if uremail[check+1:-1] == "yandex.ru":
        mail_lib = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        mail_lib.ehlo()

        try:

            urpassword = urpassword[:-1]
            uremail = uremail[:-1]
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

    elif uremail[check+1:-1] == "osteomed.ru":

        mail_lib = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        mail_lib.ehlo()

        try:

            urpassword = urpassword[:-1]
            uremail = uremail[:-1]
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