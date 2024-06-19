# Delimiters
# sep and end to format

num1 = 10
num2 = 20
num3 = 30

print('Without Seperator')
print('......................')
print('The numbers : ', num1, num2, num3)  # without seperator

# Displaying with seperators
print('\n\nWith Seperators')
print('......................')
print('The numbers : ', num1, num2, num3, sep='*')
print('The numbers : ', num1, num2, num3, sep='**')
print('The numbers : ', num1, num2, num3, sep='$$')

print('\n\n\n\nWithout End')
print('......................')

# Displaying the output with no end
print('My name is ')
print('Sujan')

# Displaying the output with 'end'
print('\n\nWith End')
print('......................')
print('My name is ', end=' ')
print('Sujan')
