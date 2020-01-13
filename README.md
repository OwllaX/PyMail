![PyMail](https://github.com/OwllaX/PyMail/blob/master/images/PyMail.png)
# PyMail
Send emails with Python and its library called 'smtplib' of easy way.

## Description
This project works to send emails with Python, giving the necessary functions for executing the send process. No generate more codes and save time!

### Prerequisites
* Install Python. You can get it on the next website: https://www.python.org/downloads/
* Use the console or GUI

### Installing
* Just need to have a system with python, put all this library in your project and follow the steps of **Running the tests**

## Running the tests
You can run it on the file 'Testing.py' and the path is:
```
../PyMail/src/Testing.py
```
But first, you need to configure some parameters
```
HOST_ADDRESS = 'SMTP.EXAMPLE.COM' # Set the smtp address
PORT_SMTP = 0 # Set the port number
MY_ADDRESS = 'youraddress@example.com' # Set your address to send the email
MY_PASSWORD = 'yourP@ssword' # Set your password
TYPE_MIMETEXT = 'plain' # Set the type of text that will have the body. OPTIONS: 'plain', 'html'
REPLY_ADDRESS = '' # If you wanna set the reply address
```
All these parameters are in the file Config.py and the path ...
```
../PyMail/src/Config.py
```
Finally, in the file 'Testing.py' just edit ...
```
add_body('This is a test') # Add the text of the body.
add_ToAddress('toAddress@example.com') # Add the address to who will be sent the email, can be one or more addresses.
add_Subject('Testing') # Add the subject of the email.
add_file('attachment') # Add one or more files in the email with the repetition of this function.

#The function 'send_mail()' returns a boolean value, where 'True' is 'sent message' and 'False' is 'Not sent message'
if send_mail():
    print('Sent Message')
else:
    print('Not sent Message')
```
And run it!

## Deployment
Just need python in whatever system that supports it.

## Built With
* [Atom] (https://atom.io/) - Text Editor
* [Python] (https://www.python.org/downloads/) - Language
* [IDE-Python] (https://atom.io/packages/ide-python) - Package for IDE of Python on Atom
* [atom-run-python] (https://atom.io/packages/atom-python-run) - Package for Run Python on Atom

## Version
* **1.0**

## Authors
* **Axalon 'OwllaX' Vargas** - *Founder and Developer* - [OwllaX] (https://github.com/OwllaX)

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
