from repository.file_repository import FileRepository
from repository.api_repository import ApiRepository
from entities.city import City
from entities.weather import Weather
import sys
import os
import asyncio

class Service:
    file_repository = FileRepository()
    api_repository = ApiRepository()

    @staticmethod
    def init_files():
        for path in [FileRepository.city_data_file, FileRepository.weather_data_file]:
            if not os.path.exists(path):            
                with open(path, "w", encoding="utf-8") as file:
                    file.write("[]")

    @staticmethod
    def run_module():
        while True:
            try:
                Service.display_start_page()

                n = Service.read_option()
                Service.dispatch_message(n)
            except Exception as e:
                print(e)
            finally:
                print("-----------------------------------------") 
            
    @staticmethod
    def display_start_page():
        print()
        print("1. ახალი ამინდის მიღება")
        print("2. რამდენიმე ქალაქის ამინდის პარალელურად (ასინქრონულად) მიღება")
        print("3. ამინდის ისტორიის გამოტანა")
        print("4. ქალაქების სია")
        print("5. ქალაქის დამატება")
        print("6. ქალაქის შეცვლა")
        print("7. ქალაქის წაშლა")
        print("8. გამოსვლა(exit)")
		
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
        if n == 1: #ახალი ამინდის მიღება
            Service.get_city_new_weather()
            
        elif n == 2: #რამდენიმე ქალაქის ამინდის პარალელურად (ასინქრონულად) მიღება
            Service.get_city_weather_history()
            
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

    @staticmethod
    def get_all_city_names():
        city_names = Service.file_repository.get_all_city_names()
        print("\n Stored cities:")
        for name in city_names:
            print("    ", name)

    @staticmethod
    def add_city():
            city_name = input("Enter the city name: ")

            city = Service.file_repository.get_city_data_by_name(city_name, raise_error = False)
            if city != None:
                raise Exception(f"City with the name '{city_name}' already exists")

            new_city = Service.api_repository.get_city_data(city_name)

            Service.file_repository.add_city(new_city)

            print(f"\n City with the name '{new_city.name}' has added\n")
		
    @staticmethod
    def edit_city():
        city_name = input("Enter the city name: ")

        city = Service.file_repository.get_city_data_by_name(city_name, raise_error = True)
        if city == None:
            raise Exception(f"City with the name '{city_name}' already exists")

        id = city.id
        new_city = Service.api_repository.get_city_data(city_name)
                
        Service.file_repository.edit_city(id, new_city)

        print(f"\n City with the name '{city.name}' has changed\n")

    @staticmethod
    def delete_city():
        name = input("Enter the city name: ")
        city = Service.file_repository.get_city_data_by_name(name)
        Service.file_repository.delete_city(city.id)
        print(f"\n City with the name '{city.name}' has deleted\n")
		
    @staticmethod
    def get_city_new_weather():
        name = input("Enter the city name: ")
        weather = Service.repository.get_city_new_weather(name)

        print(f"\nCurrent weather for the city: {name}")
        print(f"    latitude: {weather.latitude}")
        print(f"    longitude: {weather.longitude}")
        print(f"    elevation: {weather.elevation}")
        print(f"    feature_code: {weather.feature_code}")
        print(f"    country_code: {weather.country_code}")
        print(f"    admin1_id: {weather.admin1_id}")
        print(f"    admin2_id: {weather.admin2_id}")
        print(f"    timezone: {weather.timezone}")
        print(f"    population: {weather.population}")
        print(f"    country_id: {weather.country_id}")
        print(f"    country: {weather.country}")
        print(f"    admin1: {weather.admin1}")
        print(f"    admin2: {weather.admin2}")
        print(f"    generationtime_ms: {weather.generationtime_ms}")

    @staticmethod
    def get_multiple_city_new_weathers():        
        if __name__ == "service.service":            
            names = []
            weather = asyncio.run(Service.repository.get_multiple_city_new_weathers_async(names))



    @staticmethod
    def get_city_weather_history():
        name = input("Enter the city name: ")
        weather_list = Service.repository.get_city_weather_history(name)

        print(f"\n{name}'s weather data:")
        for weather in weather_list:            
            print(f"\n    weather data id={weather.get("id")}:")
            print(f"        latitude: {weather.get("latitude")}")
            print(f"        longitude: {weather.get("longitude")}")
            print(f"        elevation: {weather.get("elevation")}")
            print(f"        feature_code: {weather.get("feature_code")}")
            print(f"        country_code: {weather.get("country_code")}")
            print(f"        admin1_id: {weather.get("admin1_id")}")
            print(f"        admin2_id: {weather.get("admin2_id")}")
            print(f"        timezone: {weather.get("timezone")}")
            print(f"        population: {weather.get("population")}")
            print(f"        country_id: {weather.get("country_id")}")
            print(f"        country: {weather.get("country")}")
            print(f"        admin1: {weather.get("admin1")}")
            print(f"        admin2: {weather.get("admin2")}")
            print(f"        generationtime_ms: {weather.get("generationtime_ms")}")        