from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.deps import get_db, get_current_user
from models.meal_plan import MealPlan
from models.user import User
from schemas.meal_plan import (
    MealPlanCreate,
    MealPlanResponse,
    MealPlanUpdate
)
from datetime import date, datetime, time


router = APIRouter(
    prefix="/meal-plans",
    tags=["Meal Plans"]
)


@router.post(
    "/",
    response_model=MealPlanResponse
)
def create_meal_plan(
    meal_plan: MealPlanCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_meal_plan = MealPlan(
        user_id=current_user.id,
        food_id=meal_plan.food_id,
        meal_type=meal_plan.meal_type,
        quantity=meal_plan.quantity,
        serving_unit=meal_plan.serving_unit,
        planned_date=meal_plan.planned_date,
        notes=meal_plan.notes
    )

    db.add(new_meal_plan)
    db.commit()
    db.refresh(new_meal_plan)

    return new_meal_plan

@router.get(
    "/",
    response_model=list[MealPlanResponse]
)
def get_meal_plans(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    meal_plans = (
        db.query(MealPlan)
        .filter(MealPlan.user_id == current_user.id)
        .order_by(MealPlan.planned_date)
        .all()
    )

    return meal_plans

@router.get(
    "/date",
    response_model=list[MealPlanResponse]
)
def get_meal_plans_by_date(
    planned_date: date,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    start_datetime = datetime.combine(
        planned_date,
        time.min
    )

    end_datetime = datetime.combine(
        planned_date,
        time.max
    )

    meal_plans = (
        db.query(MealPlan)
        .filter(
            MealPlan.user_id == current_user.id,
            MealPlan.planned_date >= start_datetime,
            MealPlan.planned_date <= end_datetime
        )
        .order_by(MealPlan.planned_date)
        .all()
    )

    return meal_plans

@router.get(
    "/{meal_plan_id}",
    response_model=MealPlanResponse
)
def get_meal_plan(
    meal_plan_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    meal_plan = (
        db.query(MealPlan)
        .filter(
            MealPlan.id == meal_plan_id,
            MealPlan.user_id == current_user.id
        )
        .first()
    )

    if not meal_plan:
        raise HTTPException(
            status_code=404,
            detail="Meal plan not found"
        )

    return meal_plan

@router.put(
    "/{meal_plan_id}",
    response_model=MealPlanResponse
)
def update_meal_plan(
    meal_plan_id: int,
    meal_plan_data: MealPlanUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    meal_plan = (
        db.query(MealPlan)
        .filter(
            MealPlan.id == meal_plan_id,
            MealPlan.user_id == current_user.id
        )
        .first()
    )

    if not meal_plan:
        raise HTTPException(
            status_code=404,
            detail="Meal plan not found"
        )

    if meal_plan_data.food_id is not None:
        meal_plan.food_id = meal_plan_data.food_id

    if meal_plan_data.meal_type is not None:
        meal_plan.meal_type = meal_plan_data.meal_type

    if meal_plan_data.quantity is not None:
        meal_plan.quantity = meal_plan_data.quantity

    if meal_plan_data.serving_unit is not None:
        meal_plan.serving_unit = meal_plan_data.serving_unit

    if meal_plan_data.planned_date is not None:
        meal_plan.planned_date = meal_plan_data.planned_date

    if meal_plan_data.notes is not None:
        meal_plan.notes = meal_plan_data.notes

    db.commit()
    db.refresh(meal_plan)

    return meal_plan

@router.delete(
    "/{meal_plan_id}"
)
def delete_meal_plan(
    meal_plan_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    meal_plan = (
        db.query(MealPlan)
        .filter(
            MealPlan.id == meal_plan_id,
            MealPlan.user_id == current_user.id
        )
        .first()
    )

    if not meal_plan:
        raise HTTPException(
            status_code=404,
            detail="Meal plan not found"
        )

    db.delete(meal_plan)
    db.commit()

    return {
        "message": "Meal plan deleted successfully"
    }