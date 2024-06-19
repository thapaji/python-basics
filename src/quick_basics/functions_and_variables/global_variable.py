# Global Variable
pi = 3.143


def main():
    radius = float(input('Enter radius of circle : '))
    print('value of pi : ', pi)
    calculate_area(radius)


def calculate_area(radius):
    print('Area of circle is : ', pi * radius ** 2)


main()
