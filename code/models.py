from sqlmodel import SQLModel, Field

class FoodItem(SQLModel, table=True):
    
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    description: str | None
    in_stock: bool = Field(default=True)