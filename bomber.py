import requests
from threading import Thread
import random
import smtplib as sl

f = True
logo = '''
        ////                                         \\\\\\                             .
    ////                                                 \\\\\\                         .
////                                                         \\\\\\                     .
       ________________                    _________________                            .
      /                 \\                /                  \\                         .
     /       _           \\              /       _            \\                        .
    |       |_|           |      /      |      |_|            |                         .
     \                   /      /       \                    /                          .
      \_________________/      /__       \__________________/                           .
                                                                                        .
                            By shaby                                                    .

'''
print(logo)
#phone = input()
def send_mail(gmail, text, snd_mail, snd_pass):
    server = sl.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(snd_mail, snd_pass)
    server.sendmail(snd_mail, gmail, text)
    server.quit()
if __name__ == '__main__':
    gmail = input('Enter to bomb: ')
    n = int(input('iteration: '))
    txt = input('msg txt:')
    mail_sender = input('enter sender mail: ')
    passw = input('Your password: ')
    for i in range(n):
        send_mail(gmail, txt, mail_sender, passw)

