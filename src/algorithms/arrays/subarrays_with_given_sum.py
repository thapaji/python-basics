my_list = [20, 100, 20, 1, 10, 30, 45, 55, 67, 79, 98]


def get_sub_array_with_sum(arr, sum_to_find):
    result = []
    for item in arr:
        result.append(item)
        if sum(result) == sum_to_find:
            return result
        if sum(result) > sum_to_find:
            result.pop(0)
    return []


target_sum = 21
my_arr = get_sub_array_with_sum(my_list, target_sum)
print(f'The algorithm returned {my_arr}')
