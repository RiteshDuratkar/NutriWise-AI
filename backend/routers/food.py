from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.deps import get_db
from models.food import Food
from schemas.food import FoodCreate, FoodResponse


router = APIRouter(
    prefix="/foods",
    tags=["Foods"]
)


@router.post(
    "/",
    response_model=FoodResponse
)
def create_food(
    food: FoodCreate,
    db: Session = Depends(get_db)
):
    new_food = Food(
        name=food.name,
        category=food.category,
        serving_size=food.serving_size,
        serving_unit=food.serving_unit,
        calories=food.calories,
        protein=food.protein,
        carbohydrates=food.carbohydrates,
        fat=food.fat,
        sugar=food.sugar,
        fiber=food.fiber
    )

    db.add(new_food)
    db.commit()
    db.refresh(new_food)

    return new_food


@router.get(
    "/",
    response_model=list[FoodResponse]
)
def get_foods(
    db: Session = Depends(get_db)
):
    foods = db.query(Food).all()
    return foods


@router.get(
    "/search",
    response_model=list[FoodResponse]
)
def search_foods(
    name: str,
    db: Session = Depends(get_db)
):
    foods = (
        db.query(Food)
        .filter(Food.name.ilike(f"%{name}%"))
        .all()
    )

    return foods


@router.get(
    "/{food_id}",
    response_model=FoodResponse
)
def get_food(
    food_id: int,
    db: Session = Depends(get_db)
):
    food = (
        db.query(Food)
        .filter(Food.id == food_id)
        .first()
    )

    if not food:
        raise HTTPException(
            status_code=404,
            detail="Food not found"
        )

    return food