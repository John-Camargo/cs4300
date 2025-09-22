# task7.py

# import numpy to show off capabilities of array creation and organization
import numpy as np

# function that creates a 2D numpy array given integer dimensions of the array (n x m)
def create_2d_array(n=None, m=None):
    # print(f"n: {type(n)} and m: {type(m)}\n\n")
    # check if given dimensions are ints
    if type(n) is int and type(m) is int:
        # if so, create and reurn array
        array = np.zeros((n, m))
        # print(array)
        return array
    # check if args were both passed
    elif n is None or m is None:
        # if not, return error message
        return "Must pass both n (row) and m (col) dimensions to function."
    # else, return error message
    else:
        return "Both n and m (row/col dimension inputs) must be an integer."

# function that prints a provided numpy array, if no array provided, alternative message printed
def print_array(arr=None):
    # checks if array was provided/passed to function
    if arr is None:
        # if not, print nothing to print message
        print("No array provided, nothing to print!")
    # checks if provided array is not a numpy array
    elif not isinstance(arr, np.ndarray):
        # if so, print alternative message
        print("Array must be a numpy array.")
    # else, print array
    else:
        print(arr)

# function that adds two numpy arrays
def add_arrays(arr1 = None, arr2 = None):
    # check if arrays were passed to function
    if arr1 is None or arr2 is None:
        return "Must pass two numpy arrays to function."
    # check if both arrays are numpy arrays
    elif isinstance(arr1, np.ndarray) and isinstance(arr2, np.ndarray):
        # check that arrays have the same dimensions
        if arr1.shape[0] == arr2.shape[0] and arr2.shape[1] == arr2.shape[1]:
            # if so, add them together and return the new array
            new_arr = arr1 + arr2
            return new_arr
    # if one or neither of the arrays are numpy arrays, return error message
    else:
        return "Arrays must both be numpy type arrays"


# print(create_2d_array(5))
# print(create_2d_array())
# print(create_2d_array("",""))

# print_array(create_2d_array(4,5))
# print_array([1,2,3,4,5])