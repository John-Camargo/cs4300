# import sys and os to establish path to task file
import sys, os

# establish path to task file for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task5 import get_books, print_books, first_three_books, get_student_dict, print_student_dict, get_id_by_name, get_name_by_id

# function that tests if get_books() properly gets (returns) a list of books (which is a list of tuples)
def test_get_books():
    books = [
        ("Hatchet","Gary Paulsen"),
        ("Harry Potter and the Sorcerer's Stone","J.K. Rowling"),
        ("The Hunger Games","Suzanne Collins"),
        ("The Lightning Theif","Rick Riordan"),
        ("Rodrick Rules","Jeff Kinney"),
    ]
    book_list = get_books()
    assert books == book_list

# function that tests print_books() by capturing stdout and comparing that to the list of books (from get_books, in string form)
def test_print_books(capsys):
    print_books()
    # capture stdout/stderr (from print_books()) using capsys
    captured = capsys.readouterr()
    # compare stdout (using captured.out) and the string form of get_books() (list)
    assert captured.out == f"{get_books()}\n"


# function that tests that first_three_books() returns a list with 3 specific book titles
def test_first_three_books():
    # get list of books
    book_list = get_books()
    # ensure first_three_books() only prints the first 3 books in the list of books
    assert first_three_books(book_list) == ["Hatchet", "Harry Potter and the Sorcerer's Stone", "The Hunger Games"]
    # ensure first_three_books() returns a list with 3 elements
    assert len(first_three_books(book_list)) == 3

# function that tests that get_student_dict() gets (returns) a student dictionary
def test_get_student_dict():
    # dictionary of students with corresponding IDs (who all happen to be on the Broncos)
    student_dict = {
        "Patrick Surtain": 2,
        "Bo Nix": 10,
        "Courtland Sutton": 14,
        "J.K. Dobbins": 27,
        "Nik Bonitto": 15,
    }
    student_db = get_student_dict()
    assert student_dict == student_db

# function that tests print_books() by capturing stdout and comparing that to the list of books (from get_books(), in string form)
def test_print_student_dict(capsys):
    print_student_dict()
    # capture stdout/stderr (from print_student_dict()) using capsys
    captured = capsys.readouterr()
    # compare stdout (using captured.out) and the string form of get_student_dict() (dictionary)
    assert captured.out == f"{get_student_dict()}\n"

# fucntion that tests if get_id_by_name() returns valid ids from a given name in a student dictionary
def test_get_id_by_name():
    # get the student dictionary using get_student_dict()
    student_dict = get_student_dict()
    # test that a valid name input returns a valid corresponding id
    assert get_id_by_name("Bo Nix") == 10
    # tests for invalid input (e.g. non-existent name, wrong input type)
    assert get_id_by_name("Russel Wilson") == "No student with that name."
    assert get_id_by_name(10) == "No student with that name."

# fucntion that tests if get_name_by_id() returns valid names from a given id in a student dictionary
def test_get_name_by_id():
    # get the student dictionary using get_student_dict()
    student_dict = get_student_dict()
    # test that a valid id input returns a valid corresponding name
    assert get_name_by_id(14) == "Courtland Sutton"
    # tests for invalid input (e.g. non-existent id, wrong input type)
    assert get_name_by_id(99) == "No student with that id."
    assert get_name_by_id("Ten") == "No student with that id."
