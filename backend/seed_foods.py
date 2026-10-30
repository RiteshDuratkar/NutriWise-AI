from database.database import SessionLocal
from models.food import Food


foods = [
    # -------------------------
    # PULSES & LEGUMES
    # -------------------------
    {
        "name": "Toor Dal (Cooked)",
        "category": "Dal & Pulses",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 112,
        "protein": 7.2,
        "carbohydrates": 17.8,
        "fat": 1.0,
        "sugar": 1.0,
        "fiber": 4.0,
    },
    {
        "name": "Moong Dal (Cooked)",
        "category": "Dal & Pulses",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 105,
        "protein": 7.0,
        "carbohydrates": 17.5,
        "fat": 0.4,
        "sugar": 1.0,
        "fiber": 4.0,
    },
    {
        "name": "Masoor Dal (Cooked)",
        "category": "Dal & Pulses",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 116,
        "protein": 9.0,
        "carbohydrates": 20.0,
        "fat": 0.4,
        "sugar": 1.8,
        "fiber": 7.9,
    },
    {
        "name": "Rajma (Cooked)",
        "category": "Dal & Pulses",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 127,
        "protein": 8.7,
        "carbohydrates": 22.8,
        "fat": 0.5,
        "sugar": 0.3,
        "fiber": 6.4,
    },
    {
        "name": "Chole / Chickpeas (Cooked)",
        "category": "Dal & Pulses",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 164,
        "protein": 8.9,
        "carbohydrates": 27.4,
        "fat": 2.6,
        "sugar": 4.8,
        "fiber": 7.6,
    },

    # -------------------------
    # RICE & GRAINS
    # -------------------------
    {
        "name": "White Rice (Cooked)",
        "category": "Rice & Grains",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 130,
        "protein": 2.7,
        "carbohydrates": 28.2,
        "fat": 0.3,
        "sugar": 0.1,
        "fiber": 0.4,
    },
    {
        "name": "Brown Rice (Cooked)",
        "category": "Rice & Grains",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 123,
        "protein": 2.7,
        "carbohydrates": 25.6,
        "fat": 1.0,
        "sugar": 0.2,
        "fiber": 1.6,
    },
    {
        "name": "Poha",
        "category": "Breakfast",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 158,
        "protein": 3.0,
        "carbohydrates": 27.0,
        "fat": 4.0,
        "sugar": 1.5,
        "fiber": 1.5,
    },
    {
        "name": "Upma",
        "category": "Breakfast",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 150,
        "protein": 3.5,
        "carbohydrates": 23.0,
        "fat": 5.0,
        "sugar": 1.5,
        "fiber": 2.0,
    },

    # -------------------------
    # ROTI & BREAD
    # -------------------------
    {
        "name": "Chapati",
        "category": "Indian Breads",
        "serving_size": 40,
        "serving_unit": "g",
        "calories": 104,
        "protein": 3.1,
        "carbohydrates": 18.0,
        "fat": 2.0,
        "sugar": 0.5,
        "fiber": 2.5,
    },
    {
        "name": "Roti",
        "category": "Indian Breads",
        "serving_size": 40,
        "serving_unit": "g",
        "calories": 104,
        "protein": 3.1,
        "carbohydrates": 18.0,
        "fat": 2.0,
        "sugar": 0.5,
        "fiber": 2.5,
    },
    {
        "name": "Paratha",
        "category": "Indian Breads",
        "serving_size": 60,
        "serving_unit": "g",
        "calories": 180,
        "protein": 4.0,
        "carbohydrates": 28.0,
        "fat": 6.0,
        "sugar": 1.0,
        "fiber": 3.0,
    },

    # -------------------------
    # SOUTH INDIAN
    # -------------------------
    {
        "name": "Idli",
        "category": "South Indian",
        "serving_size": 40,
        "serving_unit": "g",
        "calories": 58,
        "protein": 2.0,
        "carbohydrates": 12.0,
        "fat": 0.2,
        "sugar": 0.2,
        "fiber": 1.0,
    },
    {
        "name": "Dosa",
        "category": "South Indian",
        "serving_size": 80,
        "serving_unit": "g",
        "calories": 168,
        "protein": 4.0,
        "carbohydrates": 28.0,
        "fat": 4.0,
        "sugar": 0.5,
        "fiber": 1.5,
    },
    {
        "name": "Sambar",
        "category": "South Indian",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 70,
        "protein": 3.5,
        "carbohydrates": 10.0,
        "fat": 2.0,
        "sugar": 2.0,
        "fiber": 3.0,
    },

    # -------------------------
    # DAIRY & PROTEIN
    # -------------------------
    {
        "name": "Paneer",
        "category": "Dairy",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 265,
        "protein": 18.3,
        "carbohydrates": 1.2,
        "fat": 20.8,
        "sugar": 1.2,
        "fiber": 0.0,
    },
    {
        "name": "Curd",
        "category": "Dairy",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 61,
        "protein": 3.5,
        "carbohydrates": 4.7,
        "fat": 3.3,
        "sugar": 4.7,
        "fiber": 0.0,
    },
    {
        "name": "Milk",
        "category": "Dairy",
        "serving_size": 100,
        "serving_unit": "ml",
        "calories": 61,
        "protein": 3.2,
        "carbohydrates": 4.8,
        "fat": 3.3,
        "sugar": 4.8,
        "fiber": 0.0,
    },

    # -------------------------
    # VEGETABLES
    # -------------------------
    {
        "name": "Potato (Boiled)",
        "category": "Vegetables",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 87,
        "protein": 1.9,
        "carbohydrates": 20.1,
        "fat": 0.1,
        "sugar": 0.9,
        "fiber": 1.8,
    },
    {
        "name": "Spinach (Cooked)",
        "category": "Vegetables",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 23,
        "protein": 2.9,
        "carbohydrates": 3.8,
        "fat": 0.4,
        "sugar": 0.4,
        "fiber": 2.4,
    },
    {
        "name": "Carrot",
        "category": "Vegetables",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 41,
        "protein": 0.9,
        "carbohydrates": 9.6,
        "fat": 0.2,
        "sugar": 4.7,
        "fiber": 2.8,
    },
    {
        "name": "Tomato",
        "category": "Vegetables",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 18,
        "protein": 0.9,
        "carbohydrates": 3.9,
        "fat": 0.2,
        "sugar": 2.6,
        "fiber": 1.2,
    },

    # -------------------------
    # FRUITS
    # -------------------------
    {
        "name": "Banana",
        "category": "Fruits",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 89,
        "protein": 1.1,
        "carbohydrates": 22.8,
        "fat": 0.3,
        "sugar": 12.2,
        "fiber": 2.6,
    },
    {
        "name": "Apple",
        "category": "Fruits",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 52,
        "protein": 0.3,
        "carbohydrates": 13.8,
        "fat": 0.2,
        "sugar": 10.4,
        "fiber": 2.4,
    },
    {
        "name": "Guava",
        "category": "Fruits",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 68,
        "protein": 2.6,
        "carbohydrates": 14.3,
        "fat": 1.0,
        "sugar": 8.9,
        "fiber": 5.4,
    },
    {
        "name": "Papaya",
        "category": "Fruits",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 43,
        "protein": 0.5,
        "carbohydrates": 10.8,
        "fat": 0.3,
        "sugar": 7.8,
        "fiber": 1.7,
    },

    # -------------------------
    # SNACKS
    # -------------------------
    {
        "name": "Roasted Chana",
        "category": "Snacks",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 364,
        "protein": 19.0,
        "carbohydrates": 60.0,
        "fat": 5.0,
        "sugar": 10.0,
        "fiber": 17.0,
    },
    {
        "name": "Peanuts",
        "category": "Nuts & Seeds",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 567,
        "protein": 25.8,
        "carbohydrates": 16.1,
        "fat": 49.2,
        "sugar": 4.7,
        "fiber": 8.5,
    },
        {
        "name": "Samosa",
        "category": "Indian Food",
        "serving_size": 100,
        "serving_unit": "g",
        "calories": 262,
        "protein": 5.0,
        "carbohydrates": 32.0,
        "fat": 13.0,
        "sugar": 1.5,
        "fiber": 2.0,
    },
]


def seed_foods():
    db = SessionLocal()

    try:
        added = 0
        skipped = 0

        for food_data in foods:
            existing_food = (
                db.query(Food)
                .filter(Food.name == food_data["name"])
                .first()
            )

            if existing_food:
                skipped += 1
                continue

            new_food = Food(**food_data)

            db.add(new_food)
            added += 1

        db.commit()

        print("Food database seeding completed.")
        print(f"Foods added: {added}")
        print(f"Foods skipped: {skipped}")

    except Exception as error:
        db.rollback()
        print("Food database seeding failed.")
        print(f"Error: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_foods()