# test_task7.py

# import sys and os to establish path to task file
# - also import numpy to test features and random to test output array from add_array()
import sys, os, numpy as np, random

# establish path to task file for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# import all functions from task file
from task7 import create_2d_array, print_array, add_arrays

# fucntion that tests the create_2d_array() function for correct output, array dimensions, and size
def test_create_2d_array():
    # ensure created array is all 0s
    assert create_2d_array(4, 5).all() == 0
    # ensure inputs are valid
    assert create_2d_array() == "Must pass both n (row) and m (col) dimensions to function."
    assert create_2d_array(5) == "Must pass both n (row) and m (col) dimensions to function."
    assert create_2d_array("","") == "Both n and m (row/col dimension inputs) must be an integer."
    assert create_2d_array(10000, 10000).any() == 0
    # ensure create_2d_array() creates the proper shape of array
    assert create_2d_array(2, 3).shape == (2, 3)
    # ensure create_2d_array() creates the proper dimensions for the array
    assert create_2d_array(4, 5).ndim == 2
    # ensure create_2d_array() creates the right size array
    assert create_2d_array(2, 5).size == 10
    # ensure create_2d_array() creates the proper type of array
    assert isinstance(create_2d_array(2, 5), np.ndarray)

# function that tests the stout ouput of print_array()
def test_print_array(capsys):
    # create arrays for different test/edge cases
    arr = create_2d_array(3, 3)
    arr1 = [1, 2, 3, 4, 5]
    arr2 = create_2d_array(0,0)
    arr3 = create_2d_array(10000, 10000)
    # get stdout from print_array()
    print_array(arr)
    # capture stdout/stderr (from print_array()) using capsys
    captured = capsys.readouterr()
    # compare stdout (using captured.out) and the string form of create_2d_array() (list)
    assert captured.out == f"{create_2d_array(3,3)}\n" 
    # repeat above process with different arrays
    # non-numpy array
    print_array(arr1)
    captured = capsys.readouterr()
    assert captured.out == "Array must be a numpy array.\n"
    # array with 0 rows/cols
    print_array(arr2)
    captured = capsys.readouterr()
    assert captured.out == f"{create_2d_array(0, 0)}\n"
    # array with large amount of rows/cols
    print_array(arr3)
    captured = capsys.readouterr()
    assert captured.out == f"{create_2d_array(10000, 10000)}\n"

# function that tests the add_arrays function for proper addition
def test_add_arrays():
    # create two arrays for testing
    arr1 = create_2d_array(2, 2)
    arr2 = create_2d_array(2, 2)
    # range for loops to use (only one var needed since arrays/matrices square)
    x = arr1.shape[0]
    # fill array/matrix with values
    for i in range(x):
        for j in range(x):
            # fill each array w/ 10 or 20 respectively
            arr1[i][j] += 10
            arr2[i][j] += 20
    # create new array, add arrays
    new_arr = add_arrays(arr1, arr2)
    # ensure array results consistent
    assert new_arr[random.randint(0,1)][random.randint(0,1)] == 30
        