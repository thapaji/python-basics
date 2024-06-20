# value error

def main():
    res = 'y'
    while res == 'y' or res == 'Y':
        try:
            num1 = int(input('Enter a number : '))
            print('You entered : ', num1)
        except ValueError:
            print('Please enter only integer number')
        res = input('Do you want to repeat ? (y/n) : ')


main()
