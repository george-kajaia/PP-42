from service.BookManager import BookManager
import sys

class MenuManager:    
    # მთავარი მეთოდი--------------------------------------------------
    @staticmethod
    def run_module():
        while True:
            try:
                MenuManager.display_main_menu()

                n = MenuManager.read_menu_option()
                MenuManager.dispatch_message(n)
            except Exception as e:
                print(e)
            finally:
                print("-----------------------------------------") 

    # ეკრანზე გამოაქვს მენიუ -------------------------------------------
    @staticmethod
    def display_main_menu():
        print()
        print("1. Add a new book")
        print("2. Get all books")
        print("3. Get the book by title")
        print("4. Exit")

    # კითხულობს კლიენტის რისი გაკეთება აირჩია ------------------------
    @staticmethod
    def read_menu_option():
        n = input("\nChoose option: ")
        if not n.isdigit():
            raise ValueError("Choose only digits")
        
        n = int(n)
        if n < 1 and n > 10:
            raise ValueError("Option must be between 1 and 10")
        
        return n

    # კლიენტის არჩეული მოქმედების შესაბამისი მეთოდის გამოძახება -------
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