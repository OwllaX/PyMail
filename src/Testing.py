from PyMail import *
add_body('Esto es una prueba')
add_ToAddress('axel72avs@gmail.com')
add_Subject('Prueba con archivos')

add_file('A:\Repos\Web\PyMail\TestFiles\Test.txt')

if send_mail():
    print('Mensaje enviado')
else:
    print('Mensaje no enviado')
