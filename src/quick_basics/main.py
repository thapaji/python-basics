to_minutes = 24 * 60
name_of_unit = 'minutes'


def main():
    while True:
        days = input('Enter list of number of days: ')
        if days == 'exit':
            break
        for day in days.split(', '):
            if validate_input(day):
                print(days_to_units(int(day)))


def days_to_units(num_of_days):
    if num_of_days == 0:
        return 'Days cannot be Zero.'
    return f'{num_of_days} days are {num_of_days * to_minutes} {name_of_unit}'


def validate_input(user_input):
    if user_input.isdigit():
        return True
    print('Not a valid number ...........')
    return False


main()
