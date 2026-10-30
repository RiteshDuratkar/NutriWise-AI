from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class FoodHistoryCreate(BaseModel):
    food_id: int
    quantity: float
    meal_type: Optional[str] = None

class FoodHistoryResponse(BaseModel):
    id: int
    user_id: int
    food_id: int
    food_name: Optional[str] = None
    quantity: float
    meal_type: Optional[str] = None

    calories: Optional[float] = None
    protein: Optional[float] = None
    carbohydrates: Optional[float] = None
    fat: Optional[float] = None

    recommendation: Optional[str] = None
    compatibility_score: Optional[float] = None

    consumed_at: Optional[datetime] = None

    class Config:
        from_attributes = True