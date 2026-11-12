from repository.file_repository import FileRepository
from Infrastructure.weather_api import WeatherApi
from entities.city import City
from entities.weather import Weather
import sys
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

class Service:
    file_repository = FileRepository()
    weather_api = WeatherApi()

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
                Service.display_main_menu()

                n = Service.read_menu_option()
                Service.dispatch_message(n)
            except Exception as e:
                print(e)
            finally:
                print("-----------------------------------------") 
            
    @staticmethod
    def display_main_menu():
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

    @staticmethod
    def get_all_city_names():
        city_names = Service.file_repository.get_all_city_names()
        print("\n Stored cities:")
        for name in city_names:
            print("    ", name)

    @staticmethod
    def add_city():
            city_name = input("Enter the city name: ")

            city = Service.file_repository.get_city_data_by_name(city_name)
            if city != None:
                raise Exception(f"City with the name '{city_name}' already exists")

            new_city = Service.weather_api.get_city_data(city_name)

            Service.file_repository.add_city(new_city)

            print(f"\n City with the name '{new_city.name}' has added\n")
		
    @staticmethod
    def edit_city():
        city_name = input("Enter the city name: ")

        city = Service.file_repository.get_city_data_by_name(city_name)
        if city == None:
            raise Exception(f"City with the name '{city_name}' does not exists")

        id = city.id
        new_city = Service.weather_api.get_city_data(city_name)
                
        Service.file_repository.edit_city(id, new_city)

        print(f"City with the name '{city.name}' has changed\n")

    @staticmethod
    def delete_city():
        city_name = input("Enter the city name: ")

        city = Service.file_repository.get_city_data_by_name(city_name)
        if city == None:
            raise Exception(f"City with the name '{city_name}' does not exists")

        Service.file_repository.delete_city(city.id)
        
        Service.file_repository.delete_city_weather(city.id)

        print(f"City with the name '{city.name}' has deleted\n")
		
    @staticmethod
    def get_city_weather():
        city_name = input("Enter the city name: ")
        
        city = Service.file_repository.get_city_data_by_name(city_name)
        if city == None:
            raise Exception(f"City with the name '{city_name}' does not exists")

        weather = Service.weather_api.get_city_whether(city)
        
        Service.file_repository.add_city_weather(weather)

        Service.__print_weather(city_name, [weather])

    @staticmethod
    def get_multiple_city_new_weathers():
        names_lat = input("Enter city names separated by commas: ").split(",")
        names_lat = [n_lat.strip() for n_lat in names_lat if n_lat.strip() != ""]
        if len(names_lat) == 0:
            raise ValueError("Enter the city names!")

        cities: list[City] = []
        for n_lat in names_lat:
            city = Service.file_repository.get_city_data_by_name(n_lat)
            if city is None:
                raise ValueError(f"City with name '{n_lat}' not found")
            cities.append(city)

        results = asyncio.run(Service.weather_api.get_multiple_city_weathers_async(cities))

        for city, result in zip(cities, results):
            if isinstance(result, BaseException):
                print(f"\nCould not get weather for '{city.name_lat}': {result}")
                continue

            Service.file_repository.add_city_weather(result)
            Service.__print_weather(city.name_lat, [result])

    @staticmethod
    def get_city_weather_history():
        name = input("Enter the city name: ")
        weather_list = Service.file_repository.get_city_weather_history(name)

        print(f"\n{name}'s weather data:")
        Service.__print_weather(name, weather_list)


    @staticmethod
    def __print_weather(city_name, weathers: list[Weather]):
        for weather in weathers:        
            print(f"\nCurrent weather for the city: {city_name}")
            print(f"    latitude: {weather.latitude}")
            print(f"    longitude: {weather.longitude}")
            print(f"    generationtime_ms: {weather.generationtime_ms}")
            print(f"    utc_offset_seconds: {weather.utc_offset_seconds}")
            print(f"    timezone: {weather.timezone}")
            print(f"    timezone_abbreviation: {weather.timezone_abbreviation}")
            print(f"    elevation: {weather.elevation}")

            print(f"    current_units-time: {weather.current_units.time}")
            print(f"    current_units-interval: {weather.current_units.interval}")
            print(f"    current_units-temperature_2m: {weather.current_units.temperature_2m}")
            print(f"    current_units-wind_speed_10m: {weather.current_units.wind_speed_10m}")
            print(f"    current_units-weather_code: {weather.current_units.weather_code}")
        
            print(f"    current-time: {weather.current.time}")
            print(f"    current-interval: {weather.current.interval}")
            print(f"    current-temperature_2m: {weather.current.temperature_2m}")
            print(f"    current-wind_speed_10m: {weather.current.wind_speed_10m}")
            print(f"    current-weather_code: {weather.current.weather_code}")
