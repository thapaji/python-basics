def main():
    my_list = [1, 2, 3, 4, 0, -4, 7, 8, 9]
    print(f'The max product of the array is : {max_product(my_list)}')


def max_product(my_list):
    res = max(my_list)
    cur_min, cur_max = 1,1
    for i in my_list:
        if i == 0:
            cur_min, cur_max = 1, 1
            continue
        temp = cur_max * i
        cur_max = max(i * cur_max, i * cur_min, i)
        cur_min = min(temp, i * cur_min, i)
        res = max(res, cur_max, cur_min)
    return res


main()
