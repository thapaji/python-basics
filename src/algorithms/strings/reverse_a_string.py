def main():
    my_string = 'I am a developer'
    print(f'The string {my_string} when reversed becomes {string_reverse(my_string)}')


def string_reverse(in_string):
    reversed_string = ''
    j = len(in_string) - 1
    while j >= 0:
        reversed_string += in_string[j]
        j -= 1
    return reversed_string


main()
