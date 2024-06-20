# for loop with step

START = 60
END = 131
INCREMENT = 10
CONVERSION_FACTOR = 0.6214


def main():
    print('KMPH\tMPH')
    print('..............')

    for kmph in range(START, END, INCREMENT):
        mph = kmph * CONVERSION_FACTOR
        print(kmph, '\t', format(mph, '.1f'))


main()
