# Comments in python are written with #
"""
    This is a multiline comment
    generally used to explain a code block.
    List datatype :- allows duplicate values
    Set datatype :- does not provide duplicate values
"""
# Lists
my_list = ['January', 'February', 'March']
print(my_list[0])
my_list.append('April')
print(my_list)

# Sets
new_list = [20, 30, 40, 50, 10, 20, 30, 40]
print('The list we declared is :::::::::::::: ')
print(new_list)
print(type(new_list))

# 1 is duplicate here which is removed automatically
my_set = {1, 2, 3, 4, 5, 1}
print('The set we declared is ////////////////// ')
print(my_set)
print((type(my_set)))
my_set.add(6)
# Does not add duplicate item
my_set.add(5)

# Sets can only be accessed using loop
print('Sets can only be accessed using loop')
for elm in my_set:
    print(elm)

new_set = set(new_list)
print('The set we converted is ////////////////// ')
print(new_set)
print((type(new_set)))
