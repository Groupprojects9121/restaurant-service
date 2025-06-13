from pydantic import BaseModel
from code.enumeration import FoodType

class FoodRequestModel(BaseModel):
    name: str
    description: str


class FoodResponseModel(BaseModel):
    name: str
    description: str 
    in_stock: bool

    class config:
        orm_mode = True


class RestaurantRequestModel(BaseModel):
    name: str 
    description: str
    food_type: FoodType