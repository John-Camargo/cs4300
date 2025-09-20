import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task6 import word_count

# function that tests if the word_count() function returns the proper word count givern both the default
# (src/task6_read_me.txt) text file and other text files. Also checks that return value is an integer
def test_word_count():
    # ensure proper word count given specific and test file(s)
    assert word_count() == 104
    assert word_count("src/task6_random_text.txt") == 33
    # ensure return value of word_count() is an int
    assert type(word_count()) is int