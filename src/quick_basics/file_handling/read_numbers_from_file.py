# read numbers from the file

def main():
    file = open('numbers.txt', 'r')

    num1 = int(file.readline().rstrip('\n'))
    num2 = int(file.readline().rstrip('\n'))
    num3 = int(file.readline().rstrip('\n'))

    print(str(num1))
    print(str(num2))
    print(str(num3))


main()
