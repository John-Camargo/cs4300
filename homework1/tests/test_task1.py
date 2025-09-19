import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task1 import printString

def test_printString():
    assert printString() == "Hello, World!"