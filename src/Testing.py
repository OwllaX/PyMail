from PyMail import *
add_body('Esto es una prueba')
add_ToAddress('axel72avs@gmail.com')
add_Subject('Esto es una prueba html')

if send_mail():
    print('Mensaje enviado')
else:
    print('Mensaje no enviado')