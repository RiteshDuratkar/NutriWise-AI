from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class WaterIntakeCreate(BaseModel):
    amount: float
    unit: Optional[str] = "ml"


class WaterIntakeResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    unit: str
    consumed_at: datetime

    class Config:
        from_attributes = True