from repository.repository import Repository
from entities.entities import City
import sys
import os

class Service:
    repository = Repository()

    @staticmethod
    def init_files():
        for path in [Repository.city_data_file, Repository.weather_data_file]:
            if not os.path.exists(path):            
                with open(path, "w", encoding="utf-8") as file:
                    file.write("[]")


    @staticmethod
    def run_module():
        while True:
            #try:
            Service.display_start_page()

            n = Service.read_option()
            Service.dispatch_message(n)
            #except Exception as e:
                #print(e)
            #finally:
            print("-----------------------------------------") 
            
    @staticmethod
    def display_start_page():
        print()
        print("1. ახალი ამინდის მიღება")
        print("2. რამდენიმე ქალაქის ამინდის პარალელურად (ასინქრონულად) მიღება")
        print("3. ამინდის ისტორიის გამოტანა")
        print("4. ქალაქის დამატება")
        print("5. ქალაქის შეცვლა")
        print("6. ქალაქის წაშლა")
        print("7. გამოსვლა(exit)")
		
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

        elif n == 4: #ქალაქის დამატება            
            Service.add_city()

        elif n == 5: #ქალაქის შეცვლა
            Service.edit_city()

        elif n == 6:  #ქალაქის წაშლა
            Service.delete_city()

        elif n == 7: #Exit
            sys.exit()
        else:
            raise ValueError("Unknown option")
            
    @staticmethod
    def add_city():
            name = input("Enter the city name: ")

            country = input("Enter the country name: ")

            latitude = input("Enter the latitude: ")
            if not latitude.isnumeric():
                raise ValueError("latitude must be a number") 
            latitude = float(latitude)
            if latitude < 0:
                raise ValueError("latitude must be greater then zero") 
            
            longitude = input("Enter the longitude: ")
            if not longitude.isnumeric():
                raise ValueError("longitude must be a number") 
            longitude = float(latitude)
            if longitude < 0:
                raise ValueError("longitude must be greater then zero") 

            city = City(0, name, country, latitude, longitude)

            Service.repository.add_city(city)

            print(f"\n City with the name '{city.name}' has added\n")
		
    @staticmethod
    def edit_city():
        name = input("Enter the city name: ")
        city = Service.repository.get_city_data_by_name(name)
               
        new_name = input("Enter the new city name: ")
        if new_name == "":
            new_name = city.name
		
        new_country = input("Enter the new country name: ")
        if new_country == "":
            new_country = city.country

        new_latitude = input("Enter the new latitude: ")
        if new_latitude == "":
            new_latitude = city.latitude
        elif not new_latitude.isnumeric():
            raise ValueError("The new latitude must be a number") 
        
        new_latitude = float(new_latitude)

        if new_latitude < 0:
            raise ValueError("The new latitude must be greater then zero") 
            
        new_longitude = input("Enter the new longitude: ")
        if new_longitude == "":
            new_longitude = city.longitude
        elif not new_longitude.isnumeric():
            raise ValueError("The new longitude must be a number") 
			
        new_longitude = float(new_longitude)
        if new_longitude < 0:
            raise ValueError("The new longitude must be greater then zero") 

        new_city = City(city.id, new_name, new_country, new_latitude, new_longitude)
        
        Service.repository.edit_city(city.id, new_city)

        print(f"\n City with the name '{city.name}' has changed\n")

    @staticmethod
    def delete_city():
        name = input("Enter the city name: ")
        city = Service.repository.get_city_data_by_name(name)
        Service.repository.delete_city(city.id)
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