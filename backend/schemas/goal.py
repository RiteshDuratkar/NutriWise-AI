from typing import Optional

from pydantic import BaseModel


class GoalCreate(BaseModel):
    goal_type: str
    daily_calorie_target: Optional[float] = None
    daily_protein_target: Optional[float] = None
    approach: Optional[str] = None


class GoalResponse(BaseModel):
    id: int
    user_id: int
    goal_type: str
    daily_calorie_target: Optional[float] = None
    daily_protein_target: Optional[float] = None
    approach: Optional[str] = None

    class Config:
        from_attributes = True