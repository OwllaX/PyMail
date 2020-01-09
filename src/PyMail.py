from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
msg['From'] = 'axel72avs@outlook.com'
msg['To'] = 'axel72avs@gmail.com'
msg['Subject'] = 'Esto es una prueba'

body = 'Esto es una prueba de funcionamiento'
msg.attach(MIMEText(body,'plain'))
print(msg)

server = smtplib.SMTP('SMTP.Office365.com', 587)
server.starttls()
server.login('axel72avs@outlook.com', 'fivrqkrvcocwvmae')
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
