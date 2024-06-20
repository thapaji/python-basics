# read file using readline
def main():
    file = open('philosophers.txt', 'r')

    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()

    file.close()

    print('Before removing line break')
    print('............................\n')
    print(line1)
    print(line2)
    print(line3)

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    print('After removing line break')
    print('............................\n')
    print(line1)
    print(line2)
    print(line3)


main()
