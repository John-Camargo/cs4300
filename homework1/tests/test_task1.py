# import sys and os to establish path to task file
import sys, os

# establish path to task file for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# import all functions from task file
from task1 import print_string

# function that tests (return value of) print_string()
def test_print_string():
    assert print_string() == "Hello, World!"

# function that tests print_string() by capturing stdout and comparing that to the original message ("Hello, World!")
def test_print_string_stdout(capsys):
    print_string()
    # capture stdout/stderr (from print_string()) using capsys
    captured = capsys.readouterr()
    # compare stdout (using captured.out) and the original string
    assert captured.out == "Hello, World!\n"