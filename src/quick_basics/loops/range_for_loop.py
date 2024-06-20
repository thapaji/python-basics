# for loop range extended

def main():
    start = int(input('Enter starting value : '))
    end = int(input('Enter ending value : '))
    for x in range(start, end + 1):
        print(x, '\tSquare\t', x * x)
        range_fxn()


def range_fxn():
    for x in range(5):
        print('Hello, ', x)


main()
