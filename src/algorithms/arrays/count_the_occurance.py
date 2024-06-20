my_list = [20, 100, 20, 1, 10, 20, 30, 45, 55, 67, 79, 98, 20]


# using loop
def count_occurrence(element):
    count = 0
    for item in my_list:
        if item == element:
            count += 1
    return count


def main():
    print(f'The occurrence of 20 in the list is {count_occurrence(20)}')


main()
