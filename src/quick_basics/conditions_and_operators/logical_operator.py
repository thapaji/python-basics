# loan qualifier using logical operators

MIN_SALARY = 30000
MIN_YEARS = 2


def main():
    salary = float(input('Enter your salary : '))
    no_of_years = int(input('Enter number of years employed : '))

    if salary >= MIN_SALARY and no_of_years >= MIN_YEARS:
        print('You are qualified for loan grant')
    else:
        print('You are not qualified for loan grant')


main()
