# Odd or even
DISCOUNT_RATE = 0.20


def main():
    res = 'y'
    while res == 'y' or res == 'Y':
        number = get_number()
        is_even = check_even(number)
        if is_even:
            print('The number is even')
        else:
            print('The number is odd')
        res = get_response()


def get_number():
    return int(input('Enter the number : '))


def check_even(number):
    if number % 2 == 0:
        return True
    return False


def get_response():
    return input('Do you want to check another number?(y/n)')


main()
