# calculate wage

def main():
    rate = float(input('Enter hourly rate : '))
    hours = float(input('Enter hours worked : '))
    calculate_wage(rate, hours)


def calculate_wage(rate, hours):
    print('Your wage is : ', hours * rate)


main()
