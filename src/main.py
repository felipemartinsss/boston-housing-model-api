import joblib
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class SimplifiedBostonHousingPayload(BaseModel):
    number_of_rooms: int
    lstat: int
    ptratio: int

@app.post("/predict")
async def predict(body: SimplifiedBostonHousingPayload):
    number_of_rooms = body.number_of_rooms
    lstat = body.lstat
    ptratio = body.ptratio
    model_input = [[number_of_rooms, lstat, ptratio]]
    house_value = model.predict(model_input)
    return {"house_value": house_value[0]}

if __name__ == "__main__":
    model = joblib.load("../model/random_forest.pkl")
    uvicorn.run(app, host = "127.0.0.1", port = 8000)