from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.deps import get_db, get_current_user
from models.goal import Goal
from models.user import User
from models.profile import Profile
from schemas.goal import GoalCreate, GoalResponse

from services.nutrition_calculator import (
    calculate_bmr,
    calculate_tdee,
    calculate_calorie_target,
    calculate_protein_target
)


router = APIRouter(
    prefix="/goals",
    tags=["Goals"]
)


@router.post(
    "/",
    response_model=GoalResponse
)
def create_goal(
    goal: GoalCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_goal = (
        db.query(Goal)
        .filter(Goal.user_id == current_user.id)
        .first()
    )

    if existing_goal:
        raise HTTPException(
            status_code=400,
            detail="Goal already exists for this user"
        )

    new_goal = Goal(
        user_id=current_user.id,
        goal_type=goal.goal_type,
        daily_calorie_target=goal.daily_calorie_target,
        daily_protein_target=goal.daily_protein_target,
        approach=goal.approach
    )

    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)

    return new_goal


@router.get(
    "/",
    response_model=GoalResponse
)
def get_goal(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    goal = (
        db.query(Goal)
        .filter(Goal.user_id == current_user.id)
        .first()
    )

    if not goal:
        raise HTTPException(
            status_code=404,
            detail="Goal not found"
        )

    return goal

@router.get(
    "/calorie-calculation"
)
def calculate_calories(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = (
        db.query(Profile)
        .filter(Profile.user_id == current_user.id)
        .first()
    )

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    if not all([
        profile.age,
        profile.height,
        profile.weight,
        profile.activity_level,
        profile.gender,
        profile.goal
    ]):
        raise HTTPException(
            status_code=400,
            detail="Complete profile information is required for calorie calculation"
        )

    try:
        bmr = calculate_bmr(
            weight=profile.weight,
            height=profile.height,
            age=profile.age,
            gender=profile.gender
        )

        tdee = calculate_tdee(
            bmr=bmr,
            activity_level=profile.activity_level
        )

        recommended_calories = calculate_calorie_target(
            tdee=tdee,
            goal=profile.goal
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    return {
        "bmr": round(bmr, 2),
        "tdee": round(tdee, 2),
        "goal": profile.goal,
        "recommended_daily_calories": round(
            recommended_calories,
            2
        )
    }

@router.put(
    "/calorie-target"
)
def update_calorie_target(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = (
        db.query(Profile)
        .filter(Profile.user_id == current_user.id)
        .first()
    )

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    if not all([
        profile.age,
        profile.height,
        profile.weight,
        profile.activity_level,
        profile.gender,
        profile.goal
    ]):
        raise HTTPException(
            status_code=400,
            detail="Complete profile information is required for calorie calculation"
        )

    goal = (
        db.query(Goal)
        .filter(Goal.user_id == current_user.id)
        .first()
    )

    if not goal:
        raise HTTPException(
            status_code=404,
            detail="Goal not found"
        )

    try:
        bmr = calculate_bmr(
            weight=profile.weight,
            height=profile.height,
            age=profile.age,
            gender=profile.gender
        )

        tdee = calculate_tdee(
            bmr=bmr,
            activity_level=profile.activity_level
        )

        recommended_calories = calculate_calorie_target(
            tdee=tdee,
            goal=profile.goal
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    goal.daily_calorie_target = round(
        recommended_calories,
        2
    )

    db.commit()
    db.refresh(goal)

    return {
        "message": "Personalized calorie target updated successfully",
        "bmr": round(bmr, 2),
        "tdee": round(tdee, 2),
        "goal": profile.goal,
        "recommended_daily_calories": round(
            recommended_calories,
            2
        ),
        "goal_id": goal.id,
        "daily_calorie_target": goal.daily_calorie_target
    }

@router.get(
    "/protein-calculation"
)
def calculate_protein(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = (
        db.query(Profile)
        .filter(Profile.user_id == current_user.id)
        .first()
    )

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    if not all([
        profile.weight,
        profile.goal
    ]):
        raise HTTPException(
            status_code=400,
            detail="Weight and goal are required for protein calculation"
        )

    try:
        recommended_protein = calculate_protein_target(
            weight=profile.weight,
            goal=profile.goal
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    protein_multiplier = (
        recommended_protein / profile.weight
    )

    return {
        "weight_kg": profile.weight,
        "goal": profile.goal,
        "protein_multiplier": protein_multiplier,
        "recommended_daily_protein": round(
            recommended_protein,
            2
        )
    }

@router.put(
    "/protein-target"
)
def update_protein_target(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = (
        db.query(Profile)
        .filter(Profile.user_id == current_user.id)
        .first()
    )

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    if not all([
        profile.weight,
        profile.goal
    ]):
        raise HTTPException(
            status_code=400,
            detail="Weight and goal are required for protein calculation"
        )

    goal = (
        db.query(Goal)
        .filter(Goal.user_id == current_user.id)
        .first()
    )

    if not goal:
        raise HTTPException(
            status_code=404,
            detail="Goal not found"
        )

    try:
        recommended_protein = calculate_protein_target(
            weight=profile.weight,
            goal=profile.goal
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    protein_multiplier = (
        recommended_protein / profile.weight
    )

    goal.daily_protein_target = round(
        recommended_protein,
        2
    )

    db.commit()
    db.refresh(goal)

    return {
        "message": "Personalized protein target updated successfully",
        "weight_kg": profile.weight,
        "goal": profile.goal,
        "protein_multiplier": protein_multiplier,
        "recommended_daily_protein": round(
            recommended_protein,
            2
        ),
        "goal_id": goal.id,
        "daily_protein_target": goal.daily_protein_target
    }