# local variable
def main():
    print('I am in main')
    get_name()


def get_name():
    name = input('Enter your name: ')  # name is local variable
    print('My name is ' + name)


main()
