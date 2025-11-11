def validate_int_input(func):
    def wrapper(*args, **kwargs):
        while True:
            value = func(*args, **kwargs)  
            if value.isdecimal():          
                return int(value)
            print("Invalid input! Please enter a valid integer.")
    return wrapper

@validate_int_input
def get_id(message)->int:
    return input(message)



def print_menu():
    print(f"""
Welcome to the library management program
----------------------------------------------
To create a new user,                   press 1
To create a new book,                   press 2
To search for a book by id,             press 3
To search for a book by title,          press 4
To search for a book by author,         press 5
To search for a user by id,             press 6
To view a list of available books,      press 7
To borrow a book,                       press 8
To return a book,                       press 9
To exit,                                press 0 
---------------------------------------------\n
          """)