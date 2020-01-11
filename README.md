# PyMail
Send emails with Python and its library called smtplib of easy way

## Getting Started
--Editing--

### Prerequisites
* Install Python. You can get it on the next website: https://www.python.org/downloads/
* Use the console or GUI
--Editing--

### Installing
--Editing--

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
add_body('This is a test') # Add the text of the body
add_ToAddress('toAddress@example.com') # Add the address to who will be sent the email
add_Subject('Testing') # Add the subject of the email
add_file('attachment') # Add one or more files in the email with the repetition of this function
```
And run it!

## Deployment
Just need python in whatever system that supports it

## Built With
* [Atom] (https://atom.io/) - Text Editor
* [Python] (https://www.python.org/downloads/) - Language
* [IDE-Python] (https://atom.io/packages/ide-python) - Package for IDE of Python on Atom
* [atom-run-python] (https://atom.io/packages/atom-python-run) - Package for Run Python on Atom

## Contributing
--Editing--

## Versioning
--Editing--

## Authors
* **Axalon 'OwllaX' Vargas** - *Founder and Developer* - [OwllaX] (https://github.com/OwllaX)

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details

## Acknowledgments
--Editing--
