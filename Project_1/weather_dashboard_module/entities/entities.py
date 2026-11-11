
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
    city_name: str
    city_id: int
    latitude: float
    longitude: float
    elevation: float
    feature_code: str
    country_code: str
    admin1_id: int
    admin2_id: int
    timezone: str
    population: int
    country_id: int
    country: str
    admin1: str    
    admin2: str
    generationtime_ms: str