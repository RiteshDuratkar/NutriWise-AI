from database.database import SessionLocal
from models.food import Food


db = SessionLocal()

try:
    foods = db.query(Food).order_by(Food.id).all()

    seen = set()
    deleted = 0

    for food in foods:
        if food.name in seen:
            print(f"Deleting duplicate: {food.id} - {food.name}")
            db.delete(food)
            deleted += 1
        else:
            seen.add(food.name)

    db.commit()

    print(f"\nDuplicate cleanup completed.")
    print(f"Duplicates deleted: {deleted}")

finally:
    db.close()