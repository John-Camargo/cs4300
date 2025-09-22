# import sys and os to establish path to task file
import sys, os, pytest

# establish path to task file for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# import all functions from task file
from task6 import word_count

# function that tests if the word_count() function returns the proper word count givern both the default
# (src/task6_read_me.txt) text file and other text files. Also checks that return value is an integer
def test_word_count():
    # ensure proper word count given specific and test file(s)
    assert word_count() == 104
    assert word_count("src/task6_random_text.txt") == 33
    # ensure return value of word_count() is an int
    assert type(word_count()) is int

# parameterized testing of the above
@pytest.mark.parametrize(
    # create a list of filenames and expected word counts to be used as args for the parameterized testing function
    "filename, count_expected",
    [
        (None, 104),
        ("src/task6_random_text.txt", 33)
    ]
)
# test each filename and expected word count using pytest parameterization
def test_word_count_param(filename, count_expected):
    # if no filename passed (filename is None), get word count of derfault ("src/tas6_read_me.txt")
    if filename is None:
        count = word_count()
    # else, get word count of provided file
    else:
        count = word_count(filename)
    # ensure count is correct and an integer
    assert count == count_expected
    assert isinstance(count, int)