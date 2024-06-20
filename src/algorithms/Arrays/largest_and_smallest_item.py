my_list = [20, 100, 20, 1, 10, 30, 45, 55, 67, 79, 98]

# sort the list in the list and first one is smallest and last one is the largest approach 1

my_list.sort()
print(my_list)
print(f'Smallest is {my_list[0]}')
print(f'Largest item is {my_list[-1]}')


# using min and max
print(f'Smallest using min : {min(my_list)}')
print(f'Smallest using max : {max(my_list)}')
