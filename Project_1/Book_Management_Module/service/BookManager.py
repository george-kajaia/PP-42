from repository.book_repository import BookRepository
from entities.book import Book
import os
import sys

class BookManager:
    book_repository = BookRepository()

    @staticmethod
    def init_file():        
        if not os.path.exists(BookRepository.book_data_file):            
            with open(BookRepository.book_data_file, "w", encoding="utf-8") as file:
                file.write("[]")

    @staticmethod
    def run_module():
        while True:
            try:
                BookManager.display_start_page()

                n = BookManager.read_option()
                BookManager.dispatch_message(n)
            except Exception as e:
                print(e)
            finally:
                print("-----------------------------------------") 
            
    @staticmethod
    def display_start_page():
        print()
        print("1. ახალი წიგნის დამატება სიაში")
        print("2. ყველა წიგნის სიის ჩვენება")
        print("3. წიგნის ძებნა მისი სათაურის მიხედვით")
        print("4. გამოსვლა(exit)")
		
    @staticmethod
    def read_option():
        n = input("\nChoose option: ")
        if not n.isdigit():
            raise ValueError("Choose only digits")
        
        n = int(n)
        if n < 1 and n > 10:
            raise ValueError("Option must be between 1 and 10")
        
        return n
        		
    @staticmethod
    def dispatch_message(n):
        if n == 1: #ახალი წიგნის დამატება სიაში
            BookManager.add_book()
           
        elif n == 2: #ყველა წიგნის სიის ჩვენება
            BookManager.get_all_books()

        elif n == 3: #წიგნის ძებნა მისი სათაურის მიხედვით
            BookManager.get_book_by_title()

        elif n == 4: #Exit
            sys.exit()
        else:
            raise ValueError("Unknown option")

    @staticmethod
    def get_book_by_title():
        book_title = input("Enter the book title: ")

        book = BookManager.book_repository.get_book_by_title(book_title)
        if book == None:
            raise Exception(f"book with the title '{book_title}' does not exist")
        
        print("\n Book data:")
        print(f"Title: {book.title}")
        print(f"Authors: {"; ".join(book.authors)}")
        print(f"Year: {book.year}")

    @staticmethod
    def get_all_books():
        books = BookManager.book_repository.get_all_books()
        
        print("\n Stored books:")
        for book in books:
            print(f"\nTitle: {book.title}")
            print(f"Authors: {"; ".join(book.authors)}")
            print(f"Year: {book.year}")

    @staticmethod
    def add_book():
            book_title = input("Enter the book title: ")
            if book_title.strip() == "":
                raise ValueError("Book title is empty")

            new_book = BookManager.book_repository.get_book_by_title(book_title)
            if new_book != None:
                raise Exception(f"book with the title '{book_title}' already exists")

            authors = input("Enter authors separated by commas: ").split(",")
            authors = [author.strip() for author in authors if author.strip() != ""]
            if len(authors) == 0:
                raise ValueError("Enter authors!")
            
            book_year = input("Enter the book year: ")
            if not book_year.isdigit():
                raise ValueError("Wrong year")

            book_year = int(book_year)
            if book_year < 0:
                raise ValueError("Book year must be greater the zero")

            new_book = Book(
                0,
                book_title,
                authors,
                book_year
            )
            BookManager.book_repository.add_book(new_book)

            print(f"\n book with the title '{new_book.title}' has added\n")
		
    @staticmethod
    def edit_book():
        book_title = input("Enter the book title: ")

        book = BookManager.book_repository.get_book_by_title(book_title)
        if book == None:
            raise Exception(f"book with the title '{book_title}' does not exist")

        id = book.id
        book_title = input("Enter the book title: ")
        if book_title.strip() == "":
            raise ValueError("Book title is empty")

        new_book = BookManager.book_repository.get_book_by_title(book_title)
        if new_book != None:
            raise Exception(f"book with the title '{book_title}' already exists")

        authors = input("Enter authors separated by commas: ").split(",")
        authors = [author.strip() for author in authors if author.strip() != ""]
        if len(authors) == 0:
            raise ValueError("Enter authors!")
            
        book_year = input("Enter the book year: ")
        if not book_year.isdigit():
            raise ValueError("Wrong year")

        book_year = int(book_year)
        if book_year < 0:
            raise ValueError("Book year must be greater the zero")

        new_book = Book(
            0,
            book_title,
            authors,
            book_year
        )             
        BookManager.book_repository.edit_book(id, new_book)

        print(f"book with the title '{book.title}' has changed\n")

    @staticmethod
    def delete_book():
        book_title = input("Enter the book title: ")
        book = BookManager.book_repository.get_book_by_title(book_title)
        if book == None:
            raise Exception(f"book with the title '{book_title}' does not exist")

        BookManager.book_repository.delete_book(book.id)
        print(f"book with the title '{book.title}' has deleted\n")        
