
from dataclasses import dataclass

@dataclass
class City:
    id: int
    name: str
    country: str
    latitude: float
    longitude: float    


@dataclass
class Weather:
    id: int
    city_id: int
    observed_at: str
    timezone: str
    temperature: float
    wind_speed: float
    weather_code: int