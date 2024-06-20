# this program writes data to the file

def main():
    file = open('philosophers.txt', 'w')

    file.write('John Locke\n')
    file.write('David Hume\n')
    file.write('Edmund Burke\n')

    file.close()
    print('Philosopher''s Name were written in the file...')


main()
