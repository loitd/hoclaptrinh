# for check mailserver
# Author: youtube.com/c/tranducloi
# Gửi gmail có nhiều file attach bằng python
# ---------------------------------------------------
from smtplib import SMTPException
from email.utils import COMMASPACE, formatdate
import smtplib,email,email.encoders,email.mime.text,email.mime.base
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPException
from smtplib import SMTP
import os
# for sending email

SERVER_SMTP = "smtp.gmail.com"
SERVER_SMTP_PORT = 587
TEXT_SUBTYPE = "html"
EMAIL_FROM = 'loitranduc@gmail.com'
EMAIL_PASS = 'gsbumkbckhjgebyw'
EMAIL_RECEIVER = ['tranducloi@youtube.com', 'loitranduc@youtube.com.c']

class SendEmail(object):
    """docstring for SENDMAIL"""
    def __init__(self, server=SERVER_SMTP, port=SERVER_SMTP_PORT):
        super(SendEmail, self).__init__()
        self.server = server
        self.port = port

    def __del__(self):
        pass

    def send(self, sender, subject, receivers=[], cc=[], bcc=[], content="", filexs=[], pswd=EMAIL_PASS, txttype=TEXT_SUBTYPE):
        #Create the email msg MIMEMultipart
        print("Begin sending email to {0}".format(receivers))
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = ','.join(receivers)
        msg["Cc"] = ','.join(cc)
        msg["Bcc"] = ','.join(bcc)
        msg['Date'] = formatdate(localtime=True)
        # prepare for content attachment
        body = MIMEMultipart('alternative')
        body.attach(MIMEText(content, txttype ))
        #Attach the message. Here we have a message with message header + message body
        msg.attach(body)

        #Attach excel files if exists
        for filex in filexs:
            if filex != '':
                fp = open(filex, 'rb')
                file1=email.mime.base.MIMEBase('application','vnd.ms-excel') #octet-stream
                file1.set_payload(fp.read())
                fp.close()
                email.encoders.encode_base64(file1)
                NAME_ATTACH = "attachment;filename=" + os.path.basename(filex)
                file1.add_header('Content-Disposition',NAME_ATTACH)
                # attach file1 to message
                msg.attach(file1)

        #begin sendmail
        try:
            smtpObj = SMTP(self.server, self.port)
            smtpObj.ehlo()
            smtpObj.starttls() #su dung port 587 -> starttls
            smtpObj.login(user=sender, password=pswd)
            smtpObj.sendmail(sender, receivers, msg.as_string())
            smtpObj.quit()
        except SMTPException as error:
            print("Error: unable to send email :  {err}".format(err=error))
        print("Send mail done!")

if __name__ == '__main__':
    m = SendEmail()
    m.send(sender=EMAIL_FROM, subject='abc', receivers=EMAIL_RECEIVER, content='a test subject', filexs=["./Pipfile",''])
