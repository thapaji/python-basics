# readline in loop

def main():
    file = open('sales.txt', 'r')
    line = file.readline()
    while line != '':
        file_content = line
        print(line)
        line = file.readline()
    file.close()


main()
