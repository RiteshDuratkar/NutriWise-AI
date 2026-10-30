from sqlalchemy import Column, Integer, Float, String
from database.database import Base


class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False, index=True)
    category = Column(String, nullable=True)

    serving_size = Column(Float, nullable=True)
    serving_unit = Column(String, nullable=True)

    calories = Column(Float, nullable=True)
    protein = Column(Float, nullable=True)
    carbohydrates = Column(Float, nullable=True)
    fat = Column(Float, nullable=True)

    sugar = Column(Float, nullable=True)
    fiber = Column(Float, nullable=True)