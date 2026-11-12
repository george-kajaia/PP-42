from repository.file_repository import FileRepository
from repository.api_repository import ApiRepository
import sys
import os
from concurrent.futures import ThreadPoolExecutor

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
            #try:
            Service.display_start_page()

            n = Service.read_option()
            Service.dispatch_message(n)
            #except Exception as e:
                #print(e)
            #finally:
                #print("-----------------------------------------") 
            
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

        print(f"City with the name '{city.name}' has changed\n")

    @staticmethod
    def delete_city():
        name = input("Enter the city name: ")
        city = Service.file_repository.get_city_data_by_name(name)
        Service.file_repository.delete_city(city.id)
        print(f"City with the name '{city.name}' has deleted\n")
        Service.file_repository.delete_city_weather(city.id)
		
    @staticmethod
    def get_city_new_weather():
        city_name = input("Enter the city name: ")
        city = Service.file_repository.get_city_data_by_name(city_name, raise_error=True)

        weather = Service.api_repository.get_city_whether(city)
        
        Service.file_repository.add_city_weather(weather)
        
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

    @staticmethod
    def get_multiple_city_new_weathers():
        names = []

        with ThreadPoolExecutor(max_workers=len(names)) as executor:
            new_weathers = list(executor.map(Service.api_repository.get_city_new_weather, names))

        with open(Repository.weather_data_file, "r", encoding="utf-8") as file:
            weathers = json.load(file)

        # 4. მაქს id-ის გამოთვლა
        max_id = 0
        for w in weathers:
            if w["id"] > max_id:
                max_id = w["id"]

        for weather in new_weathers:
            max_id += 1
            weather.id = max_id

            weathers.append(weather.__dict__)

        # ყველას ერთად შენახვა
        with open(Repository.weather_data_file, "w", encoding="utf-8") as file:
            json.dump(weathers, file, ensure_ascii=False, indent=4)

        return new_weathers            

    @staticmethod
    def get_city_weather_history():
        name = input("Enter the city name: ")
        weather_list = Service.file_repository.get_city_weather_history(name)

        print(f"\n{name}'s weather data:")
        for weather in weather_list:            
            print(f"\n    weather data id={weather.get("id")}:")
            print(f"        latitude: {weather.get("latitude")}")
            print(f"        longitude: {weather.get("longitude")}")
            print(f"        generationtime_ms: {weather.get("generationtime_ms")}")
            print(f"        utc_offset_seconds: {weather.get("utc_offset_seconds")}")
            print(f"        timezone: {weather.get("timezone")}")
            print(f"        timezone_abbreviation: {weather.get("timezone_abbreviation")}")
            print(f"        elevation: {weather.get("elevation")}")

            print(f"        current_units-time: {weather.get("current_units").get("time")}")
            print(f"        current_units-interval: {weather.get("current_units").get("interval")}")
            print(f"        current_units-temperature_2m: {weather.get("current_units").get("temperature_2m")}")
            print(f"        current_units-wind_speed_10m: {weather.get("current_units").get("wind_speed_10m")}")
            print(f"        current_units-weather_code: {weather.get("current_units").get("weather_code")}")

            print(f"        current-time: {weather.get("current").get("time")}")
            print(f"        current-interval: {weather.get("current").get("interval")}")
            print(f"        current-temperature_2m: {weather.get("current").get("temperature_2m")}")
            print(f"        current-wind_speed_10m: {weather.get("current").get("wind_speed_10m")}")
            print(f"        current-weather_code: {weather.get("current").get("weather_code")}")
