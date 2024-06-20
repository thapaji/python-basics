# file not found

def main():
    try:
        file = open('hello.txt', 'r')
        file.close()
        print('File found.')
    except FileNotFoundError:
        print('File not found :)')
    finally:
        print('Goodbye!!')


main()
