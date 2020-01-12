from PyMail import *
add_body('This is a test of functionality')
add_ToAddress('axel72avs@gmail.com')
add_ToAddress('josselyneponce33@gmail.com')
add_Subject('Test with attachment')

add_file('A:\Repos\Web\PyMail\TestFiles\Test.txt')
add_file('A:\Repos\Web\PyMail\TestFiles\Test2.txt')

if send_mail():
    print('Sent Message')
else:
    print('Didnt Send Message')
