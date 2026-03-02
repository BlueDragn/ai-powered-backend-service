from app.schemas import HouseInput
import joblib
import os
import pandas as pd

#Load model and scaler once when app starts
BASE_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "training", "model", "linear_regression_model.pkl")
scaler_path = os.path.join(BASE_DIR, "training", "model", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

def predict_house_price(data: HouseInput) -> float:
    #convert pydantic model to dictionary
    input_dict = data.dict()

    columns = [
        "MedInc",
        "HouseAge",
        "AveRooms",
        "AveBedrms",
        "Population",
        "AveOccup",
        "Latitude",
        "Longitude"
        ]


    #convert to dataFrame
    input_df = pd.DataFrame([input_dict])[columns]

    #Scale input
    input_scaled = scaler.transform(input_df)

    #predict
    prediction = model.predict(input_scaled)

    return float(prediction[0])


