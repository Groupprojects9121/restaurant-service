from sqlmodel import SQLModel, Field

from code.enumeration import FoodType

class FoodItem(SQLModel, table=True):
    
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    description: str | None
    in_stock: bool = Field(default=True)


class Restaurant(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    description: str = Field()
    food_type: FoodType