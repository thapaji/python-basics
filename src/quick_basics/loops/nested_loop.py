# nested loop
MAX_YEAR = 2024
MAX_MONTH = 12


def main():
    year = 2020
    while year <= MAX_YEAR:
        print('Year ', year)
        month = 1
        # while month <= MAX_MONTH:
        for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                      'August', 'September', 'October', 'November', 'December']:
            print('\tMonth ', month)
            # month += 1
        year += 1


main()
