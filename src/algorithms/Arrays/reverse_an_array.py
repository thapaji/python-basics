my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

i, j = 0, len(my_list) - 1

print(my_list[i], my_list[j])

while i < j:
    temp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp
    i += 1
    j -= 1

print(my_list)
