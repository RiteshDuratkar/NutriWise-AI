from typing import Optional
from pydantic import BaseModel


class FoodCreate(BaseModel):
    name: str
    category: Optional[str] = None

    serving_size: Optional[float] = None
    serving_unit: Optional[str] = None

    calories: Optional[float] = None
    protein: Optional[float] = None
    carbohydrates: Optional[float] = None
    fat: Optional[float] = None

    sugar: Optional[float] = None
    fiber: Optional[float] = None


class FoodResponse(BaseModel):
    id: int
    name: str
    category: Optional[str] = None

    serving_size: Optional[float] = None
    serving_unit: Optional[str] = None

    calories: Optional[float] = None
    protein: Optional[float] = None
    carbohydrates: Optional[float] = None
    fat: Optional[float] = None

    sugar: Optional[float] = None
    fiber: Optional[float] = None

    class Config:
        from_attributes = True