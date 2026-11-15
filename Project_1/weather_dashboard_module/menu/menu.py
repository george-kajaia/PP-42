from service.service import Service
import sys

class MenuManager:    

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
            
    @staticmethod
    def display_main_menu():
        print()
        print("1. Get the new weather")
        print("2. Get the new weather for multiple cities asynchronously")
        print("3. Get the weather history")
        print("4. Get the city list")
        print("5. Add the new city")
        print("6. Edit the city")
        print("7. Delete the city")
        print("8. exit")
		
    @staticmethod
    def read_menu_option():
        n = input("\nChoose option: ")
        if not n.isdigit():
            raise ValueError("Choose only digits")
        
        n = int(n)
        if n < 1 and n > 10:
            raise ValueError("Option must be between 1 and 10")
        
        return n
        		
    @staticmethod
    def dispatch_message(n):
        if n == 1: #ახალი ამინდის მიღება
            Service.get_city_weather()
            
        elif n == 2: #რამდენიმე ქალაქის ამინდის პარალელურად (ასინქრონულად) მიღება
            Service.get_multiple_city_new_weathers()
            
        elif n == 3: #ამინდის ისტორიის გამოტანა
            Service.get_city_weather_history()

        elif n == 4: #ქალაქების სია            
            Service.get_all_city_names()

        elif n == 5: #ქალაქის დამატება            
            Service.add_city()

        elif n == 6: #ქალაქის შეცვლა
            Service.edit_city()

        elif n == 7:  #ქალაქის წაშლა
            Service.delete_city()

        elif n == 8: #Exit
            sys.exit()
        else:
            raise ValueError("Unknown option")
