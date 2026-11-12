from entities.book import Book
import json

class BookRepository:
    book_data_file = "Project_1\Book_Management_Module\Data\Books.json"

    # წიგნის მონაცემების მიღება სახელით------------------------------------------------
    def get_book_by_title(self, title):
        books = BookRepository.__read_book_file_data()

        for c in books:
            if c["title"].lower() == title.strip().lower():
                return Book(
                    c.get("id"),
                    c.get("title"),
                    list(c.get("authors")),
                    c.get("year")
                    )

        return None

    # ყველა წიგნის მონაცემები----------------------------------------------------------
    def get_all_books(self):
        books_json = BookRepository.__read_book_file_data()

        books = [Book(**item) for item in books_json]

        return books

    # წიგნის დამატება------------------------------------------------------------------
    def add_book(self, new_book):
        books = BookRepository.__read_book_file_data()

        #მაქს id-ის გამოთვლა
        max_id = 0
        for c in books:
            if c["title"] == new_book.title:
                raise Exception(f"The book with this title '{new_book.title}' already exists")
            if c["id"] > max_id:
                max_id = c["id"]
        
        new_book.id = max_id + 1
        books.append(new_book.__dict__)

        with open(BookRepository.book_data_file, "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=4)

    # წიგნის შეცვლა---------------------------------------------------------------------
    def edit_book(self, id, new_book):
        books = BookRepository.__read_book_file_data()
        
        found = False
        for i in range(len(books)):
            if books[i]["id"] == id:
                new_book.id = id
                books[i] = new_book.__dict__
                found = True
                break
        
        if not found:
            raise ValueError(f"Book with id {id} not found")

        with open(BookRepository.book_data_file, "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=4)

    # წიგნის წაშლა----------------------------------------------------------------------
    def delete_book(self, id):
        books = BookRepository.__read_book_file_data()

        found = False
        for i in range(len(books)):
            if books[i]["id"] == id:
                books.pop(i)
                found = True
                break

        if not found:
            raise ValueError(f"Book with id {id} not found")

        with open(BookRepository.book_data_file, "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=4)

    # წიგნების ფაილიდან წაკითხვის დამხმარე მეთოდი
    @staticmethod
    def __read_book_file_data():
        with open(BookRepository.book_data_file, "r", encoding="utf-8") as file:
            content = file.read()

        if content.strip() == "":
            books = []
        else:
            books = json.loads(content)

        return books