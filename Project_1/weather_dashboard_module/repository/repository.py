from entities.entities import City, Weather
from dataclasses import dataclass
import json
import requests
from concurrent.futures import ThreadPoolExecutor

class Repository:
    city_data_file = "Project_1/Weather_Dashboard_Module/Data/CityData.json"
    weather_data_file = "Project_1/Weather_Dashboard_Module/Data/WeatherData.json"
    #url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=YOUR_API_KEY"
    url = "https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=ka"

    # ქალაქის დამატება------------------------------------------------------------------
    def add_city(self, city):            
        cities = Repository.__read_city_file_data()

        #მაქს id-ის გამოთვლა
        max_id = 0
        for c in cities:
            if c["id"] > max_id:
                max_id = c["id"]
            if c["name"] == city.name:
                raise Exception(f"City with this name '{city.name}' already exists")
        
        city.id = max_id + 1
        cities.append(city.__dict__)

        with open(Repository.city_data_file, "w", encoding="utf-8") as file:
            json.dump(cities, file, ensure_ascii=False, indent=4)

    #ქალაქის შეცვლა---------------------------------------------------------------------
    def edit_city(self, id, new_city):
        cities = Repository.__read_city_file_data()
        
        found = False
        for i in range(len(cities)):
            if cities[i]["id"] == id:
                new_city.id = id                  # keep the original id
                cities[i] = new_city.__dict__     # replace old data with new
                found = True
                break
        
        if not found:
            raise ValueError(f"City with id {id} not found")

        with open(Repository.city_data_file, "w", encoding="utf-8") as file:
            json.dump(cities, file, ensure_ascii=False, indent=4)

    #ქალაქის წაშლა----------------------------------------------------------------------
    def delete_city(self, id):
        cities = Repository.__read_city_file_data()

        found = False
        for i in range(len(cities)):
            if cities[i]["id"] == id:
                cities.pop(i)
                found = True
                break

        if not found:
            raise ValueError(f"City with id {id} not found")

        with open(Repository.city_data_file, "w", encoding="utf-8") as file:
            json.dump(cities, file, ensure_ascii=False, indent=4)

        weathers = Repository.__read_weather_file_data()

        found = False
        for i in range(len(weathers) - 1, -1, -1):
            if weathers[i]["city_id"] == id:
                weathers.pop(i)
                found = True

        with open(Repository.weather_data_file, "w", encoding="utf-8") as file:
            json.dump(weathers, file, ensure_ascii=False, indent=4)


    # ქალაქის მონაცემების მიღება სახელით------------------------------------------------
    def get_city_data_by_name(self, name):
        cities = Repository.__read_city_file_data()

        for c in cities:
            if c["name"].lower() == name.strip().lower():
                return City(c["id"], c["name"], c["country"], c["latitude"], c["longitude"])

        raise ValueError(f"City with name '{name}' not found")
        
    # ერთი ქალაქის მიმდინარე ამინდის გაგება---------------------------------------------
    def get_city_new_weather(self, name:str, save_data: bool = True):
        city = self.get_city_data_by_name(name)

        url = Repository.url.replace("{city_name}", name.strip())        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        result = response.json()

        data = result["results"][0]
        
        weather = Weather(
            0,
            data.get("name"),
            city.id,
            data.get("latitude"),
            data.get("longitude"),
            data.get("elevation"),
            data.get("feature_code"),
            data.get("country_code"),
            data.get("admin1_id"),
            data.get("admin2_id"),
            data.get("timezone"),
            data.get("population"),
            data.get("country_id"),
            data.get("country"),
            data.get("admin1"),
            data.get("admin2"),
            result.get("generationtime_ms")
        )

        if save_data == True:
            with open(Repository.weather_data_file, "r", encoding="utf-8") as file:
                weathers = json.load(file)

            max_id = 0
            for w in weathers:
                if w["id"] > max_id:
                    max_id = w["id"]
            
            weather.id = max_id + 1
            weathers.append(weather.__dict__)

            with open(Repository.weather_data_file, "w", encoding="utf-8") as file:
                json.dump(weathers, file, ensure_ascii=False, indent=4)

        return weather

    # რამდენიმე ქალაქის მიმდინარე ამინდის გაგება ასინქრონულად---------------------------
    async def get_city_new_weather_async(self, names: list):        
        with ThreadPoolExecutor(max_workers=len(names)) as executor:
            new_weathers = list(executor.map(self.get_city_new_weather, names))

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

    # ერთი ქალაქის ამინდის ისტორიის გაგება----------------------------------------------
    def get_city_weather_history(self, name):
        city = self.get_city_data_by_name(name)

        with open(Repository.weather_data_file, "r", encoding="utf-8") as file:
            weathers = json.load(file)

        result = []
        for w in weathers:
            if w["city_id"] == city.id:
                result.append(w)

        return result

    # ფაილში ჩაწერის დამხმარე მეთოდი
    @staticmethod
    def __read_city_file_data():
        with open(Repository.city_data_file, "r", encoding="utf-8") as file:
            content = file.read()

        if content.strip() == "":
            cities = []
        else:
            cities = json.loads(content)

        return cities

    @staticmethod
    def __read_weather_file_data():
        with open(Repository.weather_data_file, "r", encoding="utf-8") as file:
            content = file.read()

        if content.strip() == "":
            cities = []
        else:
            cities = json.loads(content)

        return cities