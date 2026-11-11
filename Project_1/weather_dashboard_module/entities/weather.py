from dataclasses import dataclass

@dataclass
class Weather:
    latitude: float
    longitude: float
    
    generationtime_ms: str
    utc_offset_seconds: int
    timezone: str
    timezone_abbreviation: str
    elevation: float
    current_units: _CurrentUnits
    current: _Current 

@dataclass
class _CurrentUnits:
    time: str
    interval: str
    temperature_2m: str
    wind_speed_10m: str
    weather_code: str

@dataclass
class _Current:
    time: str
    interval: str
    temperature_2m: float
    wind_speed_10m: float
    weather_code: int
