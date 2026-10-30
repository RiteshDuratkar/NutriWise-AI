from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database.database import Base


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    goal_type = Column(String, nullable=False)

    daily_calorie_target = Column(Float, nullable=True)
    daily_protein_target = Column(Float, nullable=True)

    approach = Column(String, nullable=True)