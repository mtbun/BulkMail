import smtplib

class mail(object):

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

	def import_email_list(self, filepath):
        self.receiver = open(filepath).read().splitlines()
        
    def send(self):
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        mail.ehlo()
        mail.login(self.sender[0],self.sender[1])
        
        for receiver in self.receiver:
            mail.sendmail(self.sender[0], receiver, self.content)
            

            

sender = ['hello_kitty@python.org', 'Th1s1sThePassW0Rd']

content = 'This is a Test Mail - sent from a tiny Python script.'

mailer = mail(sender, content)

mailer.import_email_list('email_list.txt')
mailer.send()
