# write numbers in file

def main():
    file = open('numbers.txt', 'w')

    num1 = int(input('Enter first number : '))
    num2 = int(input('Enter second number : '))
    num3 = int(input('Enter third number : '))

    file.write(str(num1) + '\n')
    file.write(str(num2) + '\n')
    file.write(str(num3) + '\n')

    file.close()

    print('Numbers written into file')


main()
