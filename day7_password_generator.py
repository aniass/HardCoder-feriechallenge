
"""
Napisz program do generowania losowych haseł o zadanej przez użytkownika długości. Hasło musi spełniać zadane 
warunki np. co najmniej jedna liczba, co najmniej po jednej dużej i małej literze. Warto skorzystać z modułów 
string i secrets.
Propozycja rozszerzenia: Po wygenerowaniu hasła skopiuj je do schowka systemowego
"""

import secrets
import string
import pyperclip


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            break
    return password


number = int(input('Type the number of at least 6 characters:'))      
create_password = generate_password(number)
print(f'Your generated password is {create_password}')

pyperclip.copy(create_password)
 