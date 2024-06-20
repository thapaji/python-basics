# multi way selection using if elif else

def main():
    marks = int(input('Enter your marks: '))
    if marks >= 90:
        print('Higher Distinction')
    elif marks >= 80:
        print('Distinction')
    elif marks >= 60:
        print('First Division')
    elif marks >= 50:
        print('Pass')
    else:
        print('Fail')


main()
