# sales price from the original price

originalPrice = float(input('Enter the original price : '))

discount = originalPrice * 0.2
salesPrice = originalPrice - discount

print('With the discount of $' + str(discount) + ' your discounted price is $' + str(salesPrice))
