my_list = [20, 100, 20, 1, 10, 30, 45, 55, 67, 79, 98]


# Merge sort
def merge_sort(arr, left, right):
    if left == right:
        return arr
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)
    return arr


def merge(arr, left, mid, right):
    left_array = arr[left:mid + 1]
    right_array = arr[mid + 1: right + 1]
    i, j, k = left, 0, 0
    while j < len(left_array) and k < len(right_array):
        if left_array[j] <= right_array[k]:
            arr[i] = left_array[j]
            j += 1
        else:
            arr[i] = right_array[k]
            k += 1
        i += 1
    while j < len(left_array):
        arr[i] = left_array[j]
        j += 1
        i += 1
    while k < len(right_array):
        arr[i] = right_array[k]
        k += 1
        i += 1


my_list = merge_sort(my_list, 0, len(my_list) - 1)

print('Sorted list :::: ', my_list)
