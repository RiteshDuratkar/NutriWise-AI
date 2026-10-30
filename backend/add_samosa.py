from database.database import SessionLocal
from models.food import Food


db = SessionLocal()

try:
    existing_food = (
        db.query(Food)
        .filter(Food.name.ilike("samosa"))
        .first()
    )

    if existing_food:
        print("Samosa already exists in the database.")
        print("Food ID:", existing_food.id)

    else:
        samosa = Food(
            name="Samosa",
            category="Indian Food",
            serving_size=100,
            serving_unit="g",
            calories=262,
            protein=5.0,
            carbohydrates=32.0,
            fat=13.0,
            sugar=1.5,
            fiber=2.0,
        )

        db.add(samosa)
        db.commit()
        db.refresh(samosa)

        print("Samosa added successfully!")
        print("Food ID:", samosa.id)

finally:
    db.close()