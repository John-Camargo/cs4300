# import sys and os to establish path to task file
import sys, os

# establish path to task file for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# import all functions from task file
from task4 import calculate_discount

# function that tests calculate_dicount with different inputs
def test_calculate_discount():
    # proper, working inputa qiuth ints, floats
    assert calculate_discount(123, 40) == 73.80
    assert calculate_discount(100, 25) == 75
    assert calculate_discount(5678.99, 35.53) == 3661.24
    # improper type/parameter inputs
    assert calculate_discount("string", 100) == 0
    assert calculate_discount(100, "string") == 0
    assert calculate_discount("string", "string") == 0
    assert calculate_discount() == 0