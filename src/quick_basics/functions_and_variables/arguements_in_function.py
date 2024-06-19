# passing arguments in functions

def main():
    print('hello from main')
    num = 5
    message(num)
    print('Goodbye from main')


def message(num):
    print('hello from message')
    print('Printing the passed argument ', num)
    print('Goodbye from message')


main()
