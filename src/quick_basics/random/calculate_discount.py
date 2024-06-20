# program to calculate selling price
DISCOUNT_RATE = 0.20


def main():
    req_price = get_regular_price()
    sale_price = req_price - get_discount(req_price)
    print('The sale price is : ', sale_price)


def get_regular_price():
    return float(input('Enter the regular selling price : '))


def get_discount(price):
    return DISCOUNT_RATE * price


main()
