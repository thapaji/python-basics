# string compare
STORED_PASSWORD = 'password'


def main():
    password = input('Enter password : ')
    if password == STORED_PASSWORD:
        print('Welcome to the system')
    else:
        print('Wrong password.......\n Access Denied')


main()
