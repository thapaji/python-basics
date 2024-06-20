# overtime pay calculations
BASE_HOURS = 40
OT_MULTIPLIER = 1.5


def main():
    # inputs
    hours_worked = float(input('Enter the hours worked : '))
    pay_rate = float(input('Enter the normal hours pay rate : '))

    if hours_worked > BASE_HOURS:
        calculate_pay_with_ot(hours_worked, pay_rate)
    else:
        calculate_pay(hours_worked, pay_rate)


def calculate_pay(hours_worked, pay_rate):
    pay = hours_worked * pay_rate
    print('Your pay is : $', pay)


def calculate_pay_with_ot(hours_worked, pay_rate):
    base_pay = BASE_HOURS * pay_rate
    ot_pay = (hours_worked - BASE_HOURS) * pay_rate * OT_MULTIPLIER
    pay = base_pay + ot_pay
    print('Your pay is : $', pay)


main()
