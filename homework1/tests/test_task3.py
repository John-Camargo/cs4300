import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task3 import pos_neg_zero, prime_numbers, sum_one_to_num

# function that tests is an inputted number is positive, negative, or zero 
# - tests functionality of pos_neg_zero()
def test_pos_neg_zero():
    # if positive, return a positive number
    assert pos_neg_zero(5) == 1
    # if negative return a negative number
    assert pos_neg_zero(-5) == -1
    # if zero, return a zero
    assert pos_neg_zero(0) == 0

# function that ensures prime_numbers() outputs the first ten prime numbers
def test_prime_numbers():
    # checks to see if output equals the first ten primes
    assert prime_numbers() == [2,3,5,7,11,13,17,19,23,29]

# function that tests sum_one_to_num() reutrns 5050 (the sum of the numbers 1 - 100) if not givrn output
def test_sum_one_to_num():
    assert sum_one_to_num() == 5050