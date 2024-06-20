# main module

import circle
import rectangle

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


def main():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input('Enter your choice : '))
        if choice == AREA_CIRCLE_CHOICE:
            radius = get_radius()
            print('The area of circle is : ', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = get_radius()
            print('The circumference of circle is : ', circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            length, breadth = get_length_breadth()
            print('The area of Rectangle is : ', rectangle.area(length, breadth))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            length, breadth = get_length_breadth()
            print('The perimeter of Rectangle is : ', rectangle.perimeter(length, breadth))
        elif choice == QUIT_CHOICE:
            print('Bye bye....')
        else:
            print('Please enter the valid option...')


def display_menu():
    print('Menu\n.....................\n')
    print('1.\tArea of Circle')
    print('2.\tCircumference')
    print('3.\tArea of Rectangle')
    print('4.\tPerimeter of Rectangle')
    print('5.\tQuit')


def get_radius():
    return float(input('Enter radius of circle : '))


def get_length_breadth():
    return float(input('Enter length of rectangle : ')), float(input('Enter breadth of rectangle : '))


main()
