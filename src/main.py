from fastapi import FastAPI, Depends
import numpy as np
import pickle
from pydantic_models import Day
from kafka.producer import KafkaProducer


with open("../data/weights.joblib", 'rb') as f:
    model = pickle.load(f)

producer = KafkaProducer('31.128.42.197:9092')


app = FastAPI()


@app.get("/health")
async def get_health():
    return '', 200


@app.post("/request/")
async def model_request(day: Day) -> float:
    day_list = list(dict(day).values())
    day_array = np.array(day_list)
    result = model.predict(day_array.reshape(1, -1))
    result = round(result[0], 3)
    day = dict(day)
    day['result'] = result
    await producer.send('save_to_db', day)
    return result

