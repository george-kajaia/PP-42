
from dataclasses import dataclass

@dataclass
class City:
    id: int
    name: str
    name_lat: str
    latitude: float
    longitude: float
    elevation: float
    feature_code: str
    country_code: str
    admin1_id: int
    timezone: str
    population: int
    country_id: int
    country: str
    admin1: str    
    generationtime_ms: str
