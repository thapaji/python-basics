# multi way selection nested if else

MIN_SALARY = 30000.00
MIN_YEARS = 2


def main():
    salary = float(input('Enter employee\'s annual salary : '))
    years_on_job = int(input('Enter number of years on job : '))

    if salary >= MIN_SALARY:
        if years_on_job >= MIN_YEARS:
            print('You qualified for loan grant.')
        else:
            print('You are not qualified for loan grant.')
    else:
        print('You are not qualified for loan grant.')


main()
