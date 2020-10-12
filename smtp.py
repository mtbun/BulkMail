import smtplib

class mail(object):

    def __init__(self, sender, content, receiver):
        self.sender = sender
        self.content = content
        self.receiver = receiver
        
    def send(self):
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        mail.ehlo()
        mail.login(self.sender[0],self.sender[1])
        for receiver in self.receiver:
            mail.sendmail(self.sender[0],receiver,self.content)
            

sender = ['mail_address', 'address_pass']
content = 'content'
receiver = ['1@example.com', '2@example.com']
sendMail = mail(sender, content, receiver)
sendMail.send()

    

#content = 'this mail sended with python'#mail.starttls()
#mail.ehlo()

#fromAddr = 'mail_Address'
#fromAddrPass = 'mail_Pass'
#toAddrs = ['mail1@blabla.com', 'mail2@blabla.com', 'mail3@blabla.com']

#mail.login(fromAddr, fromAddrPass)
#for toAddr in toAddrs:
#    mail.sendmail(fromAddr, toAddr, content)