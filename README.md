# Bulk mails
Sending bulk mails from a list with Python.
\
\
## How To Use

1. Install the required libraries.
```
pip3 install smtp
```
2. Clone this repo.
```
git clone https://github.com/mtbun/mail.git
```
3. Edit sender in the smtp.py
   For example:
```
sender = {
	'email': 'hello_kitty@python.org',
	'password': 'Th1s1sThePassW0Rd'
}
```
4. Edit content in the smtp.py
5. Edit your email_list file and add the addresses you want to send mail to
6. Run code
```
python3 smtp.py
```
