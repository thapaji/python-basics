# multi way selection using if else if

def main():
    marks = int(input('Enter your marks : '))
    if marks >= 90:
        print('Higher Distinction')
    else:
        if marks >= 80:
            print('Distinction')
        else:
            if marks >= 60:
                print('First Division')
            else:
                if marks >= 50:
                    print('Pass')
                else:
                    print('Fail')


main()
