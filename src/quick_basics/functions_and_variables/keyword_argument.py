# keyword parameters

def main():
    show_interest(rate=10.0, principal=1000, time=5)


def show_interest(principal, time, rate):
    print('Principal : ', principal)
    print('time : ', time)
    print('rate : ', rate)
    print('Interest : ', principal * time * rate / 100)


main()
