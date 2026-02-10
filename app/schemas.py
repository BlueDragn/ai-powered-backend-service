from pydantic import BaseModel, Field

class HouseInput(BaseModel):
    area_sqft: float = Field(gt=0)
    bedrooms: int = Field(ge=1)
    bathrooms: int = Field(ge=1)
    location_score: int = Field(ge=1, le=10)
    age_years: int = Field(ge=0)

