from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.deps import get_db
from models.user import User
from models.profile import Profile
from schemas.user import UserCreate, UserResponse
from schemas.profile import ProfileCreate, ProfileResponse
from auth import hash_password
from database.deps import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.post(
    "/{user_id}/profile",
    response_model=ProfileResponse
)
def create_profile(
    user_id: int,
    profile: ProfileCreate,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    existing_profile = (
        db.query(Profile)
        .filter(Profile.user_id == user_id)
        .first()
    )

    if existing_profile:
        raise HTTPException(
            status_code=400,
            detail="Profile already exists for this user"
        )

    new_profile = Profile(
        user_id=user_id,
        age=profile.age,
        height=profile.height,
        weight=profile.weight,
        activity_level=profile.activity_level,
        calorie_target=profile.calorie_target,
        goal=profile.goal,
        food_preference=profile.food_preference,
        gender=profile.gender
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return new_profile


@router.get(
    "/{user_id}/profile",
    response_model=ProfileResponse
)
def get_profile(
    user_id: int,
    db: Session = Depends(get_db)
):

    profile = (
        db.query(Profile)
        .filter(Profile.user_id == user_id)
        .first()
    )

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    return profile


@router.put(
    "/{user_id}/profile",
    response_model=ProfileResponse
)
def update_profile(
    user_id: int,
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if current_user.id != user_id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to update this profile"
        )

    existing_profile = (
        db.query(Profile)
        .filter(Profile.user_id == user_id)
        .first()
    )

    if not existing_profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    existing_profile.age = profile.age
    existing_profile.height = profile.height
    existing_profile.weight = profile.weight
    existing_profile.activity_level = profile.activity_level
    existing_profile.calorie_target = profile.calorie_target
    existing_profile.goal = profile.goal
    existing_profile.food_preference = profile.food_preference
    existing_profile.gender = profile.gender

    db.commit()
    db.refresh(existing_profile)

    return existing_profile