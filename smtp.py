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
        mail.login(self.sender['email'],self.sender['password'])
        
        for receiver in self.receiver:
            mail.sendmail(self.sender['email'], receiver, self.content)
            

            

sender = {
	'email': 'hello_kitty@python.org',
	'password': 'Th1s1sThePassW0Rd'
}

content = 'This is a Test Mail - sent from a tiny Python script.'

mailer = mail(sender, content)

mailer.import_email_list('email_list.txt')
mailer.send()
