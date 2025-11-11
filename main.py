from modules.book import Book
from modules.user import User
from modules.library import Library
from io import file_maneger
import library_maneger


def validate_int_input(func):
    def wrapper(*args, **kwargs):
        while True:
            value = func(*args, **kwargs)  
            if value.isdecimal():          
                return int(value)
            print("Invalid input! Please enter a valid integer.")
    return wrapper

@validate_int_input
def get_id()->int:
    return input("Enter an ID: ")





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

def main():
    maneger = library_maneger.Maneger()
    while True:
        print_menu()

        user_choice = input()

        match user_choice:
            case '1':
                user = maneger.creat_user()
                maneger.sign_user(user)
            case '2':
                book = maneger.creat_book()
                maneger.sign_book(book)
            case '3':
                if book := maneger.library.find_book(get_id()):
                    print(book)
            case '4':
                
            case '5':
                pass
            case '6':
                pass
            case '7':
                pass
            case '8':
                pass
            case '0':
                break
            case _:
                print("invalid input")
                continue

