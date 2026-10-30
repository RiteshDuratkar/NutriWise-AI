from fastapi import APIRouter, Depends
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from datetime import datetime, time
from database.deps import get_db, get_current_user
from models.water_intake import WaterIntake
from models.user import User
from schemas.water_intake import (
    WaterIntakeCreate,
    WaterIntakeResponse
)


router = APIRouter(
    prefix="/water-intake",
    tags=["Water Intake"]
)


@router.post(
    "/",
    response_model=WaterIntakeResponse
)
def create_water_intake(
    water_intake: WaterIntakeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_water_intake = WaterIntake(
        user_id=current_user.id,
        amount=water_intake.amount,
        unit=water_intake.unit
    )

    db.add(new_water_intake)
    db.commit()
    db.refresh(new_water_intake)

    return new_water_intake

@router.get(
    "/",
    response_model=list[WaterIntakeResponse]
)
def get_water_intake(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    water_intakes = (
        db.query(WaterIntake)
        .filter(
            WaterIntake.user_id == current_user.id
        )
        .order_by(WaterIntake.consumed_at.desc())
        .all()
    )

    return water_intakes

@router.get(
    "/daily-summary"
)
def get_daily_water_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    today = datetime.now().date()

    start_datetime = datetime.combine(
        today,
        time.min
    )

    end_datetime = datetime.combine(
        today,
        time.max
    )

    water_intakes = (
        db.query(WaterIntake)
        .filter(
            WaterIntake.user_id == current_user.id,
            WaterIntake.consumed_at >= start_datetime,
            WaterIntake.consumed_at <= end_datetime
        )
        .all()
    )

    total_water = sum(
        intake.amount
        for intake in water_intakes
        if intake.unit.lower() == "ml"
    )

    return {
        "date": today,
        "total_water_ml": total_water,
        "intake_count": len(water_intakes)
    }

@router.get(
    "/{water_intake_id}",
    response_model=WaterIntakeResponse
)
def get_water_intake_by_id(
    water_intake_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    water_intake = (
        db.query(WaterIntake)
        .filter(
            WaterIntake.id == water_intake_id,
            WaterIntake.user_id == current_user.id
        )
        .first()
    )

    if not water_intake:
        raise HTTPException(
            status_code=404,
            detail="Water intake not found"
        )

    return water_intake