from repository.book_repository import BookRepository
from entities.book import Book
import os
import sys
from datetime import datetime

class BookManager:
    book_repository = BookRepository()

    # თუ წიგნების შესანახი ფაილი არ არსებობს ქმნის თავიდან--------------
    @staticmethod
    def init_file():        
        if not os.path.exists(BookRepository.book_data_file):            
            with open(BookRepository.book_data_file, "w", encoding="utf-8") as file:
                file.write("[]")

    # ყველა წიგნის სიის ჩვენება-----------------------------------------
    @staticmethod
    def get_all_books():
        books = BookManager.book_repository.get_all_books()
        
        print("\n Stored books:")
        for book in books:
            print(f"\nTitle: {book.title}")
            print(f"Authors: {", ".join(book.authors)}")
            print(f"Year: {book.year}")

    # წიგნის ძებნა მისი სათაურის მიხედვით------------------------------
    @staticmethod
    def get_book_by_title():
        book_title = input("Enter the book title: ")

        book = BookManager.book_repository.get_book_by_title(book_title)
        if book == None:
            raise Exception(f"\nThe book with the title '{book_title}' does not exist")
        
        print("\nBook data:")
        print(f"Title: {book.title}")
        print(f"Authors: {", ".join(book.authors)}")
        print(f"Year: {book.year}")

    # წიგნის დამატება -------------------------------------------------
    @staticmethod
    def add_book():
            title = input("Enter the book title: ")
            if title.strip() == "":
                raise ValueError("The book title is empty")

            new_book = BookManager.book_repository.get_book_by_title(title)
            if new_book != None:
                raise Exception(f"The book with the title '{title}' already exists")

            authors = input("Enter authors separated by commas: ").split(",")
            authors = [author.strip() for author in authors if author.strip() != ""]
            if len(authors) == 0:
                raise ValueError("Enter the authors!")
            
            book_year = input("Enter the book year: ")
            if not book_year.isdigit():
                raise ValueError("Wrong year")

            book_year = int(book_year)

            if book_year < 0:
                raise ValueError("Book year must be greater the zero")

            current_year = datetime.now().year

            if book_year > current_year:
                raise ValueError(f"The book year must be less then or equal to {current_year}")

            new_book = Book(
                0,
                title,
                authors,
                book_year
            )
            BookManager.book_repository.add_book(new_book)

            print(f"\n book with the title '{new_book.title}' has added\n")

    # წიგნის მონაცემების შეცვლა ---------------------------------------
    @staticmethod
    def edit_book():
        title = input("Enter the book title: ")

        book = BookManager.book_repository.get_book_by_title(title)
        if book == None:
            raise Exception(f"The book with the title '{title}' does not exist")

        id = book.id

        title = input("Enter the book's new title: ")
        if title.strip() == "":
            raise ValueError("The book title is empty")

        new_book = BookManager.book_repository.get_book_by_title(title)
        if new_book != None:
            raise Exception(f"The book with the title '{title}' already exists")

        authors = input("Enter the new authors separated by commas: ").split(",")
        authors = [author.strip() for author in authors if author.strip() != ""]
        if len(authors) == 0:
            raise ValueError("Enter the new authors!")
            
        book_year = input("Enter the book's new year: ")
        if not book_year.isdigit():
            raise ValueError("Wrong year")

        book_year = int(book_year)
        if book_year < 0:
            raise ValueError("The book's new year must be greater the zero")

        current_year = datetime.now().year
        if book_year > current_year:
            raise ValueError(f"The book's new year must be less then or equal to {current_year}")

        new_book = Book(
            0,
            title,
            authors,
            book_year
        )             
        BookManager.book_repository.edit_book(id, new_book)

        print(f"book with the title '{book.title}' has changed\n")

    # წიგნის წაშლა ---------------------------------------------------
    @staticmethod
    def delete_book():
        title = input("Enter the book title: ")
        book = BookManager.book_repository.get_book_by_title(title)
        if book == None:
            raise Exception(f"The book with the title '{title}' does not exist")

        BookManager.book_repository.delete_book(book.id)
        print(f"The book with the title '{book.title}' has deleted\n")        
