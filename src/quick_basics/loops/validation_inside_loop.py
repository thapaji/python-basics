# validation

def main():
    marks = int(input('Enter a mark between 0 and 100 : '))
    while marks > 100 or marks < 0:
        print('Invalid Input ')
        marks = int(input('Enter a mark between 0 and 100 : '))
    print('You entered a valid mark')


main()
