from datetime import datetime, date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.deps import get_db, get_current_user
from models.food import Food
from models.food_history import FoodHistory
from models.user import User
from schemas.food_history import (
    FoodHistoryCreate,
    FoodHistoryResponse
)


router = APIRouter(
    prefix="/food-history",
    tags=["Food History"]
)


@router.post(
    "/",
    response_model=FoodHistoryResponse
)
def add_food_history(
    history: FoodHistoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    food = (
        db.query(Food)
        .filter(Food.id == history.food_id)
        .first()
    )

    if not food:
        raise HTTPException(
            status_code=404,
            detail="Food not found"
        )

    # Calculate nutrition based on the quantity entered by the user
    serving_size = food.serving_size or 100

    multiplier = history.quantity / serving_size

    new_history = FoodHistory(
        user_id=current_user.id,
        food_id=food.id,
        quantity=history.quantity,
        meal_type=history.meal_type,
        consumed_at=datetime.now(),

        calories=(
            food.calories * multiplier
            if food.calories is not None
            else None
        ),

        protein=(
            food.protein * multiplier
            if food.protein is not None
            else None
        ),

        carbohydrates=(
            food.carbohydrates * multiplier
            if food.carbohydrates is not None
            else None
        ),

        fat=(
            food.fat * multiplier
            if food.fat is not None
            else None
        )
    )

    db.add(new_history)
    db.commit()
    db.refresh(new_history)

    return new_history

@router.get(
    "/",
    response_model=list[FoodHistoryResponse]
)
def get_food_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    history = (
        db.query(FoodHistory, Food)
        .join(
            Food,
            Food.id == FoodHistory.food_id
        )
        .filter(
            FoodHistory.user_id == current_user.id
        )
        .all()
    )

    response = []

    for item, food in history:
        response.append(
            {
                "id": item.id,
                "user_id": item.user_id,
                "food_id": item.food_id,
                "food_name": food.name,
                "quantity": item.quantity,
                "meal_type": item.meal_type,
                "calories": item.calories,
                "protein": item.protein,
                "carbohydrates": item.carbohydrates,
                "fat": item.fat,
                "recommendation": item.recommendation,
                "compatibility_score": item.compatibility_score,
                "consumed_at": item.consumed_at
            }
        )

    return response

@router.get(
    "/daily-summary"
)
def get_daily_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    today = date.today()

    start_of_day = datetime.combine(
        today,
        datetime.min.time()
    )

    end_of_day = datetime.combine(
        today,
        datetime.max.time()
    )

    history = (
        db.query(FoodHistory)
        .filter(
            FoodHistory.user_id == current_user.id,
            FoodHistory.consumed_at >= start_of_day,
            FoodHistory.consumed_at <= end_of_day
        )
        .all()
    )

    total_calories = sum(
        item.calories or 0
        for item in history
    )

    total_protein = sum(
        item.protein or 0
        for item in history
    )

    total_carbohydrates = sum(
        item.carbohydrates or 0
        for item in history
    )

    total_fat = sum(
        item.fat or 0
        for item in history
    )

    return {
        "date": today,
        "total_calories": total_calories,
        "total_protein": total_protein,
        "total_carbohydrates": total_carbohydrates,
        "total_fat": total_fat,
        "food_count": len(history)
    }