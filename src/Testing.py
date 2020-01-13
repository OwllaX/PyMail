from PyMail import add_body, add_ToAddress, add_Subject, add_file, send_mail
add_body('This is a test of functionality')
add_ToAddress('someone1@example.com')
add_ToAddress('someone2@example.com')
add_Subject('Test with attachment')

add_file('..\TestFiles\Test.txt')
add_file('..\TestFiles\Test2.txt')

if send_mail():
    print('Sent Message')
else:
    print('Not sent Message')
