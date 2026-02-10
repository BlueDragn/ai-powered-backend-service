from fastapi import FastAPI
from app.schemas import HouseInput
from app.services import predict_house_price

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend service is up and running!"}

@app.post("/predict")
def predict_house(data: HouseInput):
    price = predict_house_price(data)
    return {
        "predicted_price": price,
        "currency": "INR"
        }