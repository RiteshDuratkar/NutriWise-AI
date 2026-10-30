from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class MealPlanCreate(BaseModel):
    food_id: Optional[int] = None
    meal_type: str
    quantity: Optional[float] = None
    serving_unit: Optional[str] = None
    planned_date: datetime
    notes: Optional[str] = None


class MealPlanUpdate(BaseModel):
    food_id: Optional[int] = None
    meal_type: Optional[str] = None
    quantity: Optional[float] = None
    serving_unit: Optional[str] = None
    planned_date: Optional[datetime] = None
    notes: Optional[str] = None


class MealPlanResponse(BaseModel):
    id: int
    user_id: int
    food_id: Optional[int] = None
    meal_type: str
    quantity: Optional[float] = None
    serving_unit: Optional[str] = None
    planned_date: datetime
    notes: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True