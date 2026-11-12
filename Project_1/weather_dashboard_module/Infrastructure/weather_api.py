import asyncio
import aiohttp
import requests
from entities.city import City
from entities.weather import Weather

class WeatherApi:
    city_url = "https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=ka"
    whether_url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m,weather_code"

    # ერთი ქალაქის მონაცემების  გაგება ---------------------------------------------
    def get_city_data(self, city_name):
        url = WeatherApi.city_url.replace("{city_name}", city_name.strip())
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        result = response.json()

        data = result["results"][0]
        
        return City(
            data.get("id"),
            data.get("name"),
            city_name,
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

    # ერთი ქალაქის მიმდინარე ამინდის გაგება ---------------------------------------
    def get_city_whether(self, city: City):
        url = WeatherApi.whether_url.replace("{latitude}", str(city.latitude)).replace("{longitude}", str(city.longitude))

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        result = response.json()

        result["id"] = 0
        result["city_id"] = city.id

        weather = Weather(**result)
        
        return weather

    # რამდენიმე ქალაქის მიმდინარე ამინდის გაგება ასინქრონულად --------------------
    async def get_multiple_city_weathers_async(self, cities: list[City]):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
            tasks = [self.__fetch_city_weather_async(session, city) for city in cities]
            return await asyncio.gather(*tasks, return_exceptions=True)

    # ამინდის გაგების ასინქრონული მეთოდი ----------------------------------------
    async def __fetch_city_weather_async(self, session: aiohttp.ClientSession, city: City):
        url = WeatherApi.whether_url.replace("{latitude}", str(city.latitude)).replace("{longitude}", str(city.longitude))

        async with session.get(url) as response:
            response.raise_for_status()
            result = await response.json()

        result["id"] = 0
        result["city_id"] = city.id

        return Weather(**result)