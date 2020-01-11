from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os.path import basename, exists
import smtplib
from Config import *

msg = MIMEMultipart() #Inicialize the message
msg['From'] = MY_ADDRESS #Insert MY_ADDRESS to the email
if REPLY_ADDRESS != '':
    msg.add_header('reply-to', REPLY_ADDRESS)

saved_files = [] #This variable is the container of all files to send

#Add files to the email
def add_file(path):
    saved_files.append(path)

#This function puts up all the files into the email
def setFiles():
    if len(saved_files) != 0:
        for filename in saved_files:
            if exists(filename):
                with open(filename, 'rb') as attachment:
                    part = MIMEBase('application', 'octec-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                filename = basename(filename)
                part.add_header('content-disposition', f"attachment; filename={filename}")
                msg.attach(part)

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
        setFiles()
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        return False
