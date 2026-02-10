from app.schemas import HouseInput
def predict_house_price(data: HouseInput) -> float:
    # dummy logic
    base_price = data.area_sqft * 5000
    location_bonus = data.location_score * 10000

    return base_price + location_bonus
