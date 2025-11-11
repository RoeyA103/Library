from modules.book import Book
from modules.user import User
from modules.library import Library
from io_utils.file_manager import *
from io_utils.ios import *
import library_manager
from time import sleep


def main():
    manager = library_manager.Manager()

    while True:
        sleep(1)
        print_menu()

        user_choice = input()

        match user_choice:
            case '1':
                user = manager.create_user()
                manager.sign_user(user)
            case '2':
                user_id = get_id("enter a user id")
                manager.delete_user(user_id)
            case '3':
                book = manager.create_book()
                manager.sign_book(book)
            case '4':
                book_isbn = get_id("enter a book isbn")
                manager.delete_book(book_isbn)
            case '5':
                book_id = get_id("enter book id:\n")
                if book := manager.library.find_book(book_id):
                    print(book)
            case '6':
                manager.library.search_book_by_title(input("enter title:\n"))
            case '7':
                manager.library.search_book_by_author(input("enter author name:\n"))
            case '8':
                user_id = get_id("enter user id:\n")
                if user := manager.library.find_user(user_id):
                    print(user)
            case '9':
                print(manager.library.list_available_books())
            case '10':
                user_id = get_id("enter user id:\n")
                book_id = get_id("enter book id:\n")
                manager.borrow_book(user_id,book_id)
            case '11':
                user_id = get_id("enter uder id:\n")
                book_id = get_id("enter book id:\n")
                manager.return_book(user_id,book_id)
            case '0':
                break
            case _:
                print("invalid input")
                continue

if __name__ == "__main__":
    main()