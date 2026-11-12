from dataclasses import dataclass

@dataclass
class CurrentUnits:
    time: str
    interval: str
    temperature_2m: str
    wind_speed_10m: str
    weather_code: str


@dataclass
class Current:
    time: str
    interval: int
    temperature_2m: float
    wind_speed_10m: float
    weather_code: int
    
@dataclass
class Weather:
    id: int
    city_id: int
    latitude: float
    longitude: float
    generationtime_ms: float
    utc_offset_seconds: int
    timezone: str
    timezone_abbreviation: str
    elevation: float
    current_units: CurrentUnits
    current: Current

    def __post_init__(self):
        if isinstance(self.current_units, dict):
            self.current_units = CurrentUnits(**self.current_units)
        if isinstance(self.current, dict):
            self.current = Current(**self.current)
