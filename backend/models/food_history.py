from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from database.database import Base


class FoodHistory(Base):
    __tablename__ = "food_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    food_id = Column(
        Integer,
        ForeignKey("foods.id"),
        nullable=False
    )

    quantity = Column(Float, nullable=False)

    meal_type = Column(String, nullable=True)

    calories = Column(Float, nullable=True)
    protein = Column(Float, nullable=True)
    carbohydrates = Column(Float, nullable=True)
    fat = Column(Float, nullable=True)

    recommendation = Column(String, nullable=True)

    compatibility_score = Column(Float, nullable=True)

    consumed_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=True
    )