from .shared import intpk, created_at
from sqlalchemy.orm import Mapped, mapped_column
from db.core import Base


class Prediction(Base):
    __tablename__ = 'prediction'

    id: Mapped[intpk] 
    season: Mapped[int]
    holiday: Mapped[int]
    workingday: Mapped[int]
    weather: Mapped[int]
    temp: Mapped[float]
    atemp: Mapped[float]
    humidity: Mapped[float]
    windspeed: Mapped[float]
    year: Mapped[int]
    month: Mapped[int]
    day: Mapped[int]
    hour: Mapped[int]
    prediction: Mapped[float]
    created_at: Mapped[created_at]
