# read using for loop

def main():
    file = open('sales.txt', 'r')
    for line in file:
        print(line)
    file.close()


main()
