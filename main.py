from fastapi import FastAPI
import numpy as np
import pickle

from src.pydantic_models import Day


with open("src/data/weights.joblib", 'rb') as f:
    model = pickle.load(f)


app = FastAPI()


@app.post("/request/")
def model_request(day: Day) -> float:
    day_list = list(dict(day).values())
    day_array = np.array(day_list)
    result = model.predict(day_array.reshape(1, -1))
    return round(result[0], 3)