from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from Config import *

msg = MIMEMultipart()
msg['From'] = MY_ADDRESS
if REPLY_ADDRESS != '':
    msg.add_header('reply-to', REPLY_ADDRESS)

#Add the address to who will be send
def add_ToAddress(toAddress):
    msg['To'] = toAddress

#Add the subject of the email
def add_Subject(subject):
    msg['Subject'] = subject

#Add the body of the email
def add_body(text):
    msg.attach(MIMEText(text,TYPE_MIMETEXT))

#This will send the email
def send_mail():
    try:
        server = smtplib.SMTP(HOST_ADDRESS, PORT_SMTP)
        server.starttls()
        server.login(MY_ADDRESS, MY_PASSWORD)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        return False
