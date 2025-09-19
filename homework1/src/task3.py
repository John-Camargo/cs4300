import math

# function that determines if passed value is positive, negative, or zero
def pos_neg_zero(x):
    # if x is greater than zero, it is positive, return 1
    if x > 0:
        return 1
    # if x is less than zero, it is negative, return -1
    elif x < 0:
        return -1
    # if x is zero, return 0
    elif x == 0:
        return 0

def prime_numbers(x=10):
    # list to store first x prime numbers
    prime_list = []
    # var to determine when to stop loop
    count = 0
    # loop/range accounts for all possible primes bounded by x^2
    #   - if x = 10, range = 2 - 100 s.t. all primes are within range (10th prime = 29)
    for num in range(2, (x * x)):
        # boolean flag representing if the current number in the given range is prime or not
        prime = True
        # divisibility check (from 2 - sqrt(num) + 1)
        for i in range(2, int(math.sqrt(num)) + 1):
            # checks if num is divisible (by all i values), if so -> not a prime #, if not -> prime #
            if num % i == 0:
                prime = False
                # breaks out of loop if num divisible by any i (as it can't be prime at that point)
                break
        # if num prime, append num to list of primes
        if prime:
            prime_list.append(num)
            # add one to one to count so len(prime_list) == x (or 10)
            count += 1
            # when count == x (10), exit main loop
            if count == x:
                break
    # print list of first x primes
    print(prime_list)
    # return list of first x primes
    return(prime_list)

# function that computes the sum of all numbers from one to x (where x here is 100)
def sum_one_to_num(x=100):
    # i is the start of the summation (1)
    i = 1
    # var for total summation
    sum = 0
    # while i (counter) is not 100, continue looping and adding
    while i <= x:
        # add current number to total sum
        sum += i
        # increment i (counter)
        i += 1
    # print and return total sum
    print(sum)
    return(sum)

# pos_neg_zero(10)
prime_numbers()
# sum_one_to_num()
