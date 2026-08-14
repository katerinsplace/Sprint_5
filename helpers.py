from random import choices
from string import ascii_lowercase, digits

symbols = ascii_lowercase + digits

def new_email_password():
    random_name = ''.join(choices(symbols, k=10)) + '@yandex.ru'
    random_password = ''.join(choices(symbols, k=8))
    return random_name, random_password

