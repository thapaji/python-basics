# loop to calculate sales commission

def main():
    keep_going = 'y'
    while keep_going == 'y':
        show_commission()
        keep_going = input('Do you want to keep going (y/n) : ')


def show_commission():
    sales = float(input('Enter Total Sales : '))
    comm_rate = float(input('Enter Commission Rate : '))
    commission = sales * comm_rate
    print('Your sales commission is : ', commission)


main()
