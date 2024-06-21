def main():
    while True:
        day = input('Enter number of days: ')
        if day == 'exit':
            break
        name_of_unit = input('Enter name of unit: ')
        days_and_unit_dictionary = {'day': day, 'unit': name_of_unit}
        if validate_input(days_and_unit_dictionary['day']):
            print(days_to_units(days_and_unit_dictionary))


def days_to_units(days_and_unit):
    calculation_unit = 0
    num_of_days = int(days_and_unit['day'])
    conversion_unit = days_and_unit['unit']
    if conversion_unit == 'hours':
        calculation_unit = 24
    elif conversion_unit == 'minutes':
        calculation_unit = 24 * 60
    elif conversion_unit == 'seconds':
        calculation_unit = 24 * 60 * 60
    else:
        return 'Invalid unit'
    if num_of_days == 0:
        return 'Days cannot be Zero.'
    return f'{num_of_days} days are {num_of_days * calculation_unit} {conversion_unit}'


def validate_input(user_input):
    if user_input.isdigit():
        return True
    print('Not a valid number ...........')
    return False


main()
