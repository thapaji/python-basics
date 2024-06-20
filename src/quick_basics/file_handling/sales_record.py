def main():
    choice = '1'
    while choice != '3':
        print('Menu')
        print('.............')
        print('1. Display All')
        print('2. Search')
        print('3. Exit')
        choice = input('Enter your menu choice : ')
        if choice == '1':
            display_all()
        elif choice == '2':
            search()


def search():
    choice = 'y'
    while choice.upper() == 'Y':
        query = input('Enter salesman to search : ')
        file = open('sales.txt', 'r')
        print('Salesman\tQuarter1\tQuarter2\tQuarter3\tQuarter4')
        print('.........................................................................')
        found = False
        for line in file:
            words = line.split()
            if query.upper() == words[0].upper():
                found = True
                print(words[0] + '\t\t' + words[1] + '\t\t' + words[2] + '\t\t' + words[3] + '\t\t' + words[4])
        if not found:
            print('Your salesman could not be found..')
        file.close()
        choice = input('Search for any particular salesman(Y/N)')


def display_all():
    file = open('sales.txt', 'r')
    print('Salesman\tQuarter1\tQuarter2\tQuarter3\tQuarter4')
    print('.........................................................................')
    for line in file:
        # print(line,sep=' ')
        words = line.split()
        print(words[0] + '\t\t' + words[1] + '\t\t' + words[2] + '\t\t' + words[3] + '\t\t' + words[4])
    file.close()


main()
