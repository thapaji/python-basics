# write some records into the sales file

def main():
    num_days = int(input('how many days sales do you want to enter : '))
    file = open('sales.txt', 'w')
    for count in range(1, num_days + 1):
        sales = float(input('Enter the sales of ' + str(count) + ' day : '))
        file.write(str(sales) + '\n')
    file.close()
    print('Sales data written successfully')


main()
