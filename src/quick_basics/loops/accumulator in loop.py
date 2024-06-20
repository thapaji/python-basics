# running total and accumulator variable

MAX = 5


def main():
    total_salary = 0.0;
    for emp in range(5):
        salary = float(input('Enter the salary of employee ' + str(emp + 1) + ' : '))
        total_salary += salary
        print('Total salary is : $', total_salary)

    print('Total salary is : $', total_salary)


main()
