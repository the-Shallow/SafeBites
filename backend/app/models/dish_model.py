from pydantic import BaseModel, Field
from typing import Optional, List

class Dish(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    ingredients: List[str]
    restaurant: str
    price: float
