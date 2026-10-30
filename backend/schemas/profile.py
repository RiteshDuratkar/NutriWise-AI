from typing import Optional
from pydantic import BaseModel


class ProfileCreate(BaseModel):
    age: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    activity_level: Optional[str] = None
    calorie_target: Optional[float] = None
    goal: Optional[str] = None
    food_preference: Optional[str] = None
    gender: Optional[str] = None


class ProfileResponse(BaseModel):
    id: int
    user_id: int
    age: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    activity_level: Optional[str] = None
    calorie_target: Optional[float] = None
    goal: Optional[str] = None
    food_preference: Optional[str] = None
    gender: Optional[str] = None

    class Config:
        from_attributes = True