# returning multiple values

def main():
    num1, num2 = get_inputs()
    total, average = calculate_numbers(num1, num2)
    output(total, average)


def get_inputs():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    return num1, num2


def calculate_numbers(num1, num2):
    total = num1 + num2
    average = total / 2
    return total, average


def output(total, average):
    print('Your total number is : ', total, '\nYour average is : ', average)


main()
