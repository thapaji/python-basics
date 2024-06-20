# single way selection
HIGH_SCORE = 95


def main():
    # get test scores
    test1 = int(input('Enter the score for test1 : '))
    test2 = int(input('Enter the score for test2 : '))
    test3 = int(input('Enter the score for test3 : '))

    # calculate the average
    average = (test1 + test2 + test3) / 3

    # output the average
    print('The average is : ', average)

    # if statement
    if average >= HIGH_SCORE:
        print('Congratulations')
        print('That is a great average')


main()
