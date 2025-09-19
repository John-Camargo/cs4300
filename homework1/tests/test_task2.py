import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task2 import Int, Float, Bool, String

def test_int():
    assert type(Int()) is int

def test_float():
    assert type(Float()) is float

def test_bool():
    assert type(Bool()) is bool

def test_string():
    assert type(String()) is str