import sys, os, pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task2 import Int, Float, Bool, String

# test that the Int() function returns the right type (int) and value
def test_int():
    assert type(Int()) is int
    assert Int() == 100

# test that the Float() function returns the right type (float) and value
def test_float():
    assert type(Float()) is float
    assert Float() == 3.33

# test that the Bool() function returns the right type (bool) and value
def test_bool():
    assert type(Bool()) is bool
    assert Bool() == False

# test that the String() function returns the right type (str) and value
def test_string():
    assert type(String()) is str
    assert String() == "String"

# parameterized testing of the above
@pytest.mark.parametrize(
    # create a list of functions and types to be used as args for the parameterized testing function
    "type_funct, type_expected",
    [
        (Int, int),
        (Float, float),
        (Bool, bool),
        (String, str),
    ]
)
# test each function and expected type using pytest parameterization
def test_types_param(type_funct, type_expected):
    # test that the function returns the propr data type
    assert isinstance(type_funct(), type_expected)
