from database.database import SessionLocal
from models.food import Food


foods = [
    {
        "name": "Biryani",
        "category": "Indian Main Course",
        "serving_size": 250,
        "serving_unit": "g",
        "calories": 450,
        "protein": 18.0,
        "carbohydrates": 55.0,
        "fat": 18.0,
        "sugar": 3.0,
        "fiber": 3.0,
    },
    {
        "name": "Butter Chicken",
        "category": "Indian Main Course",
        "serving_size": 250,
        "serving_unit": "g",
        "calories": 490,
        "protein": 31.0,
        "carbohydrates": 14.0,
        "fat": 34.0,
        "sugar": 5.0,
        "fiber": 2.0,
    },
    {
        "name": "Chicken Tikka",
        "category": "Indian Main Course",
        "serving_size": 150,
        "serving_unit": "g",
        "calories": 250,
        "protein": 35.0,
        "carbohydrates": 6.0,
        "fat": 9.0,
        "sugar": 2.0,
        "fiber": 1.0,
    },
    {
        "name": "Chana Masala",
        "category": "Indian Main Course",
        "serving_size": 200,
        "serving_unit": "g",
        "calories": 280,
        "protein": 12.0,
        "carbohydrates": 42.0,
        "fat": 7.0,
        "sugar": 6.0,
        "fiber": 11.0,
    },
    {
        "name": "Dal Tadka",
        "category": "Dal & Pulses",
        "serving_size": 200,
        "serving_unit": "g",
        "calories": 230,
        "protein": 11.0,
        "carbohydrates": 30.0,
        "fat": 7.0,
        "sugar": 2.0,
        "fiber": 8.0,
    },
    {
        "name": "Dal Makhani",
        "category": "Dal & Pulses",
        "serving_size": 200,
        "serving_unit": "g",
        "calories": 300,
        "protein": 12.0,
        "carbohydrates": 34.0,
        "fat": 13.0,
        "sugar": 4.0,
        "fiber": 9.0,
    },
    {
        "name": "Kadai Paneer",
        "category": "Paneer Dishes",
        "serving_size": 200,
        "serving_unit": "g",
        "calories": 360,
        "protein": 17.0,
        "carbohydrates": 14.0,
        "fat": 27.0,
        "sugar": 5.0,
        "fiber": 3.0,
    },
    {
        "name": "Palak Paneer",
        "category": "Paneer Dishes",
        "serving_size": 200,
        "serving_unit": "g",
        "calories": 300,
        "protein": 17.0,
        "carbohydrates": 12.0,
        "fat": 22.0,
        "sugar": 3.0,
        "fiber": 4.0,
    },
    {
        "name": "Naan",
        "category": "Indian Breads",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 310,
        "protein": 9.0,
        "carbohydrates": 50.0,
        "fat": 8.0,
        "sugar": 3.0,
        "fiber": 2.0,
    },
    {
        "name": "Bhatura",
        "category": "Indian Breads",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 330,
        "protein": 7.0,
        "carbohydrates": 45.0,
        "fat": 13.0,
        "sugar": 2.0,
        "fiber": 2.0,
    },
]


def add_indian_foods():
    db = SessionLocal()

    try:
        added = 0
        skipped = 0

        for food_data in foods:
            existing_food = (
                db.query(Food)
                .filter(Food.name.ilike(food_data["name"]))
                .first()
            )

            if existing_food:
                skipped += 1
                continue

            db.add(Food(**food_data))
            added += 1

        db.commit()

        print("Indian food database update completed.")
        print(f"Foods added: {added}")
        print(f"Foods skipped: {skipped}")

    except Exception as error:
        db.rollback()
        print("Indian food database update failed.")
        print(f"Error: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    add_indian_foods()