import smtplib

class mail(object):

    def __init__(self, sender, content, receiver):
        self.sender = sender
        self.content = content
        self.receiver = receiver
        
    def send(self):
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.starttls()
        mail.ehlo()
        mail.login(self.sender['address'], self.sender['password'])
        
        for receiver in self.receiver:
            mail.sendmail(self.sender[0], receiver, self.content)
            

sender = {
    'address': 'ethmtrgt@gmail.com',
    'password': 'thisIsMyPassw0rd'
}

# Example

content = 'This mail sent from a python script.'
receiver = ['test@gmail.com']
sendMail = mail(sender, content, receiver)
sendMail.send()
