from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    age = Column(Integer, nullable=True)
    height = Column(Float, nullable=True)
    weight = Column(Float, nullable=True)

    activity_level = Column(String, nullable=True)
    calorie_target = Column(Float, nullable=True)

    goal = Column(String, nullable=True)
    food_preference = Column(String, nullable=True)
    gender = Column(String, nullable=True)