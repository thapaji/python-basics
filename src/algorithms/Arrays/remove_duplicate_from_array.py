# remove duplicates from sorted array
def main():
    my_list = [10, 10, 20, 20, 30, 30, 40, 50, 60, 70, 80, 80, 90, 100]
    print(f'Total unique values : {remove_duplicates(my_list)}')
    print(my_list)


def remove_duplicates(my_list):
    left_index = 1
    for r in range(1, len(my_list)):
        if my_list[r] != my_list[r - 1]:
            my_list[left_index] = my_list[r]
            left_index += 1
    return left_index


main()