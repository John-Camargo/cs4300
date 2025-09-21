import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task3 import pos_neg_zero, prime_numbers, sum_one_to_num

# 
def test_pos_neg_zero():
    assert pos_neg_zero(5) == 1
    assert pos_neg_zero(-5) == -1
    assert pos_neg_zero(0) == 0

def test_prime_numbers():
    assert prime_numbers() == [2,3,5,7,11,13,17,19,23,29]

def test_sum_one_to_num():
    assert sum_one_to_num() == 5050