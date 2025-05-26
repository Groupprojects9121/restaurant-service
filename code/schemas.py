from pydantic import BaseModel


class FoodRequestModel(BaseModel):
    name: str
    description: str


class FoodResponseModel(BaseModel):
    name: str
    description: str 
    in_stock: bool

    class config:
        orm_mode = True