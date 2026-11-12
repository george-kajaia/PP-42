from entities.city import City
from entities.weather import Weather
import json
from dataclasses import asdict


class FileRepository:
    city_data_file = "Project_1/Weather_Dashboard_Module/Data/CityData.json"
    weather_data_file = "Project_1/Weather_Dashboard_Module/Data/WeatherData.json"        

    # ქალაქის დამატება------------------------------------------------------------------
    def add_city(self, new_city):
        cities = FileRepository.__read_city_file_data()

        #მაქს id-ის გამოთვლა
        max_id = 0
        for c in cities:
            if c["id"] > max_id:
                max_id = c["id"]
            if c["name_lat"] == new_city.name_lat:
                raise Exception(f"City with this name '{new_city.name_lat}' already exists")
        
        new_city.id = max_id + 1
        cities.append(new_city.__dict__)

        with open(FileRepository.city_data_file, "w", encoding="utf-8") as file:
            json.dump(cities, file, ensure_ascii=False, indent=4)

    # #ქალაქის შეცვლა---------------------------------------------------------------------
    def edit_city(self, id, new_city):
        cities = FileRepository.__read_city_file_data()
        
        found = False
        for i in range(len(cities)):
            if cities[i]["id"] == id:
                new_city.id = id
                cities[i] = new_city.__dict__
                found = True
                break
        
        if not found:
            raise ValueError(f"City with id {id} not found")

        with open(FileRepository.city_data_file, "w", encoding="utf-8") as file:
            json.dump(cities, file, ensure_ascii=False, indent=4)

    #ქალაქის წაშლა----------------------------------------------------------------------
    def delete_city(self, id):
        cities = FileRepository.__read_city_file_data()

        found = False
        for i in range(len(cities)):
            if cities[i]["id"] == id:
                cities.pop(i)
                found = True
                break

        if not found:
            raise ValueError(f"City with id {id} not found")

        with open(FileRepository.city_data_file, "w", encoding="utf-8") as file:
            json.dump(cities, file, ensure_ascii=False, indent=4)

    # # ქალაქის მონაცემების მიღება სახელით------------------------------------------------
    def get_city_data_by_name(self, name_lat):
        cities = FileRepository.__read_city_file_data()

        for c in cities:
            if c["name_lat"].lower() == name_lat.strip().lower():
                return City(
                    c.get("id"),
                    c.get("name"),
                    c.get("name_lat"),
                    c.get("latitude"),
                    c.get("longitude"),
                    c.get("elevation"),
                    c.get("feature_code"),
                    c.get("country_code"),
                    c.get("admin1_id"),
                    c.get("timezone"),
                    c.get("population"),
                    c.get("country_id"),
                    c.get("country"),
                    c.get("admin1"),
                    c.get("generationtime_ms")
                )

        return None

    # # ყველა ქალაქის სახელის გამოტანა----------------------------------------------------
    def get_all_city_names(self):
        cities = FileRepository.__read_city_file_data()

        city_names = []
        for city in cities:            
            city_names.append(city.get("name") + " - " + city.get("name_lat"))

        return city_names

    # ერთი ქალაქის ამინდის ისტორიის გაგება----------------------------------------------
    def get_city_weather_history(self, name_lat) -> list[Weather]:
        city = self.get_city_data_by_name(name_lat)
        if city is None:
            raise Exception(f"City with the name '{name_lat}' does not exist")

        weathers = FileRepository.__read_weather_file_data()

        result: list[Weather] = []
        for w in weathers:
            if w["city_id"] == city.id:
                result.append(Weather(**w))

        return result

    # ერთი ქალაქის ამინდის ჩაწერა ფაილში------------------------------------------------
    def add_city_weather(self, new_weather):        
        weathers = FileRepository.__read_weather_file_data()

        #მაქს id-ის გამოთვლა
        max_id = 0
        for c in weathers:
            if c["id"] > max_id:
                max_id = c["id"]
        
        new_weather.id = max_id + 1
        weathers.append(asdict(new_weather))

        with open(FileRepository.weather_data_file, "w", encoding="utf-8") as file:
            json.dump(weathers, file, ensure_ascii=False, indent=4)

    # ამინდის წაშლა ფაილიდან-----------------------------------------------------------
    def delete_city_weather(self, id):
        weathers = FileRepository.__read_weather_file_data()

        for i in range(len(weathers) - 1, -1, -1):
            if weathers[i]["city_id"] == id:
                weathers.pop(i)                

        with open(FileRepository.weather_data_file, "w", encoding="utf-8") as file:
            json.dump(weathers, file, ensure_ascii=False, indent=4)

    # ქალაქების ფაილიდან წაკითხვის დამხმარე მეთოდი
    @staticmethod
    def __read_city_file_data():
        with open(FileRepository.city_data_file, "r", encoding="utf-8") as file:
            content = file.read()

        if content.strip() == "":
            cities = []
        else:
            cities = json.loads(content)

        return cities

    # ამინდების ფაილიდან წაკითხვის დამხმარე მეთოდი
    @staticmethod
    def __read_weather_file_data():
        with open(FileRepository.weather_data_file, "r", encoding="utf-8") as file:
            content = file.read()

        if content.strip() == "":
            cities = []
        else:
            cities = json.loads(content)

        return cities