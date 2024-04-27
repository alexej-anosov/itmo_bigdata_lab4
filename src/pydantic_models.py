from pydantic import BaseModel, model_validator
from enum import Enum
from typing import Optional
from datetime import datetime


class Season(int, Enum):
    sprring = 1
    summer = 2
    fall = 3
    winter = 4
    
    
class Weather(int, Enum):
    clear = 1
    cloudy = 2
    light_rain = 3
    heavy_rain = 4
    
class Binary(int, Enum):
    true = 1
    false = 0
    
class Day(BaseModel):
    season: Season
    holiday: Binary
    workingday: Binary
    weather: Weather
    temp: float
    atemp: float
    humidity: float
    windspeed: float
    dt: datetime
    year: int = None
    month: int = None
    day: int = None
    hour: int = None


    @model_validator(mode='after')
    @classmethod
    def populate_full_name(cls, values):
        dt = values.dt
        values.day = dt.day
        values.month = dt.month
        values.year = dt.year
        values.hour = dt.hour
        del values.dt
        return values
