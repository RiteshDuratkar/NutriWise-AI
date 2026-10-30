from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from database.database import Base
from datetime import datetime


class WaterIntake(Base):
    __tablename__ = "water_intake"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    amount = Column(Float, nullable=False)
    unit = Column(String, nullable=False, default="ml")

    consumed_at = Column(DateTime, default=datetime.utcnow)