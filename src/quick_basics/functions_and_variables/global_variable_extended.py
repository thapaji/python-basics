# Global variable extended

my_value = 10


def main():
    print('my value ', my_value)
    show_value()
    show_value_again()
    change_global()
    print('my value ', my_value)


def show_value():
    my_value = 30
    print('my value ', my_value)


def show_value_again():
    print('my value ', my_value)


def change_global():
    global my_value
    my_value = 20
    print('my value ', my_value)


main()
