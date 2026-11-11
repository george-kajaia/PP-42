import requests
from entities.city import City
from entities.weather import Weather

class ApiRepository:
    city_url = "https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=ka"
    whether_url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m,weather_code"

    def get_city_data(self, city_name):
        url = ApiRepository.city_url.replace("{city_name}", city_name.strip())
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        result = response.json()

        data = result["results"][0]
        
        return City(
            data.get("id"),
            data.get("name"),
            data.get("latitude"),
            data.get("longitude"),
            data.get("elevation"),
            data.get("feature_code"),
            data.get("country_code"),
            data.get("admin1_id"),
            data.get("timezone"),
            data.get("population"),
            data.get("country_id"),
            data.get("country"),
            data.get("admin1"),
            data.get("generationtime_ms")
        )        

    def get_city_whether(self, city: City):
        url = ApiRepository.whether_url.replace("{latitude}", str(city.latitude)).replace("{longitude}", str(city.longitude))
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        result = response.json()

        weather = Weather(**result)
        
        return weather

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

    რამდენიმე ქალაქის მიმდინარე ამინდის გაგება ასინქრონულად---------------------------
    async def get_multiple_city_new_weathers_async(self, names: list):
        async with aiohttp.ClientSession() as session:
            tasks = [self.get_city_new_weather(name, False) for name in names]
            #return await asyncio.gather(*tasks)