# this program reads the contents of file

def main():
    file = open('philosophers.txt', 'r')

    file_contents = file.read()

    file.close()
    print(file_contents)


main()
