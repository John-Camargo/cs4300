# function that gets (returns) a list of books (which is a list of tuples)
def get_books():
    # list of my favorite books from my childhood, including the author, is a list of tuples
    book_list = [
        ("Hatchet","Gary Paulsen"),
        ("Harry Potter and the Sorcerer's Stone","J.K. Rowling"),
        ("The Hunger Games","Suzanne Collins"),
        ("The Lightning Theif","Rick Riordan"),
        ("Rodrick Rules","Jeff Kinney"),
    ]
    return book_list

# function that prints a list of books (which is a list of tuples)
def print_books():
    books = get_books()
    print(books)

# function that prints first three elements of a list of books (which is a list of tuples)
def first_three_books(books):
    # creates a list and fills list with the first element of each tuple from the list of books
    books_to_slice = [i[0] for i in books]
    print(books_to_slice[0:3])
    return (books_to_slice[0:3])


# function that gets (returns) a student dictionary
def get_student_dict():
    # dictionary of students with corresponding IDs (who all happen to be on the Broncos)
    student_dict = {
        "Patrick Surtain": 2,
        "Bo Nix": 10,
        "Courtland Sutton": 14,
        "J.K. Dobbins": 27,
        "Nik Bonitto": 15,
    }
    return student_dict

# function that prints (the contents of) a student dictoinary
def print_student_dict():
    db = get_student_dict()
    print(db)

# function that gets (returns) a student's ID by their corresponding name
def get_id_by_name(name: str):
    db = get_student_dict()
    # if the name does not exist in the student dictionary (database), output error message
    if db.get(name) == None:
        return "No student with that name."
    else:
        return db.get(name)

# function that gets (returns) a student's name by their corresponding id
def get_name_by_id(id: int):
    for curr_name, curr_id in student_dict.items():
        # if id in student dictionary (databse), return name
        if curr_id == id:
            return curr_name
        # if the id does not exist in the student dictionary (database), output error message
    return "No student with that id."

# list of my favorite books from my childhood, including the author, is a list of tuples
book_list = [
    ("Hatchet","Gary Paulsen"),
    ("Harry Potter and the Sorcerer's Stone","J.K. Rowling"),
    ("The Hunger Games","Suzanne Collins"),
    ("The Lightning Theif","Rick Riordan"),
    ("Rodrick Rules","Jeff Kinney"),
]

# dictionary of students with corresponding IDs (who all happen to be on the Broncos)
student_dict = {
    "Patrick Surtain": 2,
    "Bo Nix": 10,
    "Courtland Sutton": 14,
    "J.K. Dobbins": 27,
    "Nik Bonitto": 15,
}
# print_books()
# first_three_books(book_list)
# print_student_dict(student_dict)
# print(get_student_dict(student_dict))
print(get_id_by_name("Bo Nix"))
print(get_id_by_name("Bo Ni"))
# print(get_name_by_id(10))
# print(first_three_books(get_books()))

