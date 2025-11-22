import secrets
import string

def get_password():
    puncuation = string.punctuation
    psw = string.ascii_letters + string.digits
    password = ''
    print('-----------------------')
    psw_lenght = input('How long u want your password?: ')
    lenght = int(psw_lenght)
    special_char = input('Would u like special characters in a password (Y/N)?: ')
    if special_char.upper() == 'Y':
        psw = string.ascii_letters + string.digits + string.punctuation
    elif special_char.upper() == 'N':
        pass
    else:
        print('Invalid input. Please try again!')

    for _ in range(lenght):
        password += secrets.choice(psw)
    print(password)
        

get_password()