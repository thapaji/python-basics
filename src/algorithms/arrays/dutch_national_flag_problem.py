my_list = [0, 1, 2, 1, 2, 1, 2, 2, 1, 0, 0, 1, 0, 0, 1]


def dutch_national_flag(arr):
    start = 0
    mid = 0
    end = len(arr) - 1

    while mid <= end:
        if arr[mid] == 0:
            arr[start], arr[mid] = arr[mid], arr[start]
            start += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[end] = arr[end], arr[mid]
            end -= 1


dutch_national_flag(my_list)
print(my_list)
