from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from database.database import Base
from datetime import datetime


class MealPlan(Base):
    __tablename__ = "meal_plans"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    food_id = Column(Integer, ForeignKey("foods.id"), nullable=True)

    meal_type = Column(String, nullable=False)

    quantity = Column(Float, nullable=True)
    serving_unit = Column(String, nullable=True)

    planned_date = Column(DateTime, nullable=False)

    notes = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)