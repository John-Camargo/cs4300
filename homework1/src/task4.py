# function that calculates a total price based off of original price and discount
def calculate_discount(price, percentage):
    # validation to ensure price and percentage are numeric
    if isinstance(price, (int, float)) and isinstance(percentage, (int, float)):
        # calculate discount to be reduced from the price (convert passed number to decimal value for percentage, multiply by price)
        discount = round((price * (percentage/100)), 2)
        # calculate total by subtracting discount amount from original price
        total = round((price - discount), 2)
        # print and return total price
        print(total)
        return total
    else:
        return 0
    

# calculate_discount(100, 25)
# calculate_discount(505.50, 17.5)
# calculate_discount(100, 12.5)