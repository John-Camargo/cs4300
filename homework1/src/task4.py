# function that calculates a total price based off of original price and discount
def calculate_discount(price, percentage):
    # calculate discount to be reduced from the price (convert passed number to decimal value for percentage, multiply by price)
    discount = round((price * (percentage/100)), 2)
    # calculate total by subtracting discount amount from original price
    total = round((price - discount), 2)
    # print and return total price
    print(total)
    return total

# calculate_discount(100, 25)
# calculate_discount(505.50, 17.5)
# calculate_discount(100, 12.5)