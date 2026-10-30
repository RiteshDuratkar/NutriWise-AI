from database.database import SessionLocal
from models.food import Food


# ============================================================
# NUTRIWISE AI FOOD DATABASE
# 76 classes from the Fruit AI model
# Nutrition values are per 100g
# ============================================================

AI_FOODS = [
    {"name": "Apple", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 52, "protein": 0.3, "carbohydrates": 13.8, "fat": 0.2, "sugar": 10.4, "fiber": 2.4},
    {"name": "Apricot", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 48, "protein": 1.4, "carbohydrates": 11.1, "fat": 0.4, "sugar": 9.2, "fiber": 2.0},
    {"name": "Avocado", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 160, "protein": 2.0, "carbohydrates": 8.5, "fat": 14.7, "sugar": 0.7, "fiber": 6.7},
    {"name": "Banana", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 89, "protein": 1.1, "carbohydrates": 22.8, "fat": 0.3, "sugar": 12.2, "fiber": 2.6},
    {"name": "Beans", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 31, "protein": 1.8, "carbohydrates": 7.1, "fat": 0.2, "sugar": 3.3, "fiber": 3.4},
    {"name": "Beetroot", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 43, "protein": 1.6, "carbohydrates": 9.6, "fat": 0.2, "sugar": 6.8, "fiber": 2.8},
    {"name": "Blackberry", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 43, "protein": 1.4, "carbohydrates": 9.6, "fat": 0.5, "sugar": 4.9, "fiber": 5.3},
    {"name": "Blueberry", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 57, "protein": 0.7, "carbohydrates": 14.5, "fat": 0.3, "sugar": 10.0, "fiber": 2.4},
    {"name": "Cabbage", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 25, "protein": 1.3, "carbohydrates": 5.8, "fat": 0.1, "sugar": 3.2, "fiber": 2.5},
    {"name": "Cactus", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 16, "protein": 0.7, "carbohydrates": 3.3, "fat": 0.1, "sugar": 1.1, "fiber": 2.2},
    {"name": "Caju", "category": "Nuts & Seeds", "serving_size": 100, "serving_unit": "g", "calories": 553, "protein": 18.2, "carbohydrates": 30.2, "fat": 43.9, "sugar": 5.9, "fiber": 3.3},
    {"name": "Cantaloupe", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 34, "protein": 0.8, "carbohydrates": 8.2, "fat": 0.2, "sugar": 7.9, "fiber": 0.9},
    {"name": "Carambula", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 31, "protein": 1.0, "carbohydrates": 6.7, "fat": 0.3, "sugar": 3.9, "fiber": 2.8},
    {"name": "Carrot", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 41, "protein": 0.9, "carbohydrates": 9.6, "fat": 0.2, "sugar": 4.7, "fiber": 2.8},
    {"name": "Cauliflower", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 25, "protein": 1.9, "carbohydrates": 5.0, "fat": 0.3, "sugar": 1.9, "fiber": 2.0},
    {"name": "Cherimoya", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 75, "protein": 1.6, "carbohydrates": 17.7, "fat": 0.7, "sugar": 12.9, "fiber": 3.0},
    {"name": "Cherry", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 63, "protein": 1.1, "carbohydrates": 16.0, "fat": 0.2, "sugar": 12.8, "fiber": 2.1},
    {"name": "Chestnut", "category": "Nuts & Seeds", "serving_size": 100, "serving_unit": "g", "calories": 213, "protein": 2.4, "carbohydrates": 45.5, "fat": 2.3, "sugar": 10.6, "fiber": 8.1},
    {"name": "Clementine", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 47, "protein": 0.9, "carbohydrates": 12.0, "fat": 0.2, "sugar": 9.2, "fiber": 1.7},
    {"name": "Cocos", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 354, "protein": 3.3, "carbohydrates": 15.2, "fat": 33.5, "sugar": 6.2, "fiber": 9.0},
    {"name": "Corn", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 86, "protein": 3.3, "carbohydrates": 18.7, "fat": 1.4, "sugar": 6.3, "fiber": 2.0},
    {"name": "Cucumber", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 15, "protein": 0.7, "carbohydrates": 3.6, "fat": 0.1, "sugar": 1.7, "fiber": 0.5},
    {"name": "Dates", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 282, "protein": 2.5, "carbohydrates": 75.0, "fat": 0.4, "sugar": 63.4, "fiber": 8.0},
    {"name": "Eggplant", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 25, "protein": 1.0, "carbohydrates": 5.9, "fat": 0.2, "sugar": 3.5, "fiber": 3.0},
    {"name": "Fig", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 74, "protein": 0.8, "carbohydrates": 19.2, "fat": 0.3, "sugar": 16.3, "fiber": 2.9},
    {"name": "Ginger", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 80, "protein": 1.8, "carbohydrates": 17.8, "fat": 0.8, "sugar": 1.7, "fiber": 2.0},
    {"name": "Gooseberry", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 44, "protein": 0.9, "carbohydrates": 10.2, "fat": 0.6, "sugar": 4.9, "fiber": 4.3},
    {"name": "Granadilla", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 97, "protein": 2.2, "carbohydrates": 23.4, "fat": 0.7, "sugar": 11.2, "fiber": 10.4},
    {"name": "Grape", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 69, "protein": 0.7, "carbohydrates": 18.1, "fat": 0.2, "sugar": 15.5, "fiber": 0.9},
    {"name": "Grapefruit", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 42, "protein": 0.8, "carbohydrates": 10.7, "fat": 0.1, "sugar": 6.9, "fiber": 1.6},
    {"name": "Guava", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 68, "protein": 2.6, "carbohydrates": 14.3, "fat": 1.0, "sugar": 8.9, "fiber": 5.4},
    {"name": "Hazelnut", "category": "Nuts & Seeds", "serving_size": 100, "serving_unit": "g", "calories": 628, "protein": 15.0, "carbohydrates": 16.7, "fat": 60.8, "sugar": 4.3, "fiber": 9.7},
    {"name": "Huckleberry", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 57, "protein": 0.7, "carbohydrates": 14.5, "fat": 0.3, "sugar": 10.0, "fiber": 2.4},
    {"name": "Kaki", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 70, "protein": 0.6, "carbohydrates": 18.6, "fat": 0.2, "sugar": 12.5, "fiber": 3.6},
    {"name": "Kiwi", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 61, "protein": 1.1, "carbohydrates": 14.7, "fat": 0.5, "sugar": 9.0, "fiber": 3.0},
    {"name": "Kohlrabi", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 27, "protein": 1.7, "carbohydrates": 6.2, "fat": 0.1, "sugar": 2.6, "fiber": 3.6},
    {"name": "Kumquats", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 71, "protein": 1.9, "carbohydrates": 15.9, "fat": 0.9, "sugar": 9.4, "fiber": 6.5},
    {"name": "Lemon", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 29, "protein": 1.1, "carbohydrates": 9.3, "fat": 0.3, "sugar": 2.5, "fiber": 2.8},
    {"name": "Lychee", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 66, "protein": 0.8, "carbohydrates": 16.5, "fat": 0.4, "sugar": 15.2, "fiber": 1.3},
    {"name": "Mandarine", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 53, "protein": 0.8, "carbohydrates": 13.3, "fat": 0.3, "sugar": 10.6, "fiber": 1.8},
    {"name": "Mango", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 60, "protein": 0.8, "carbohydrates": 15.0, "fat": 0.4, "sugar": 13.7, "fiber": 1.6},
    {"name": "Mangostan", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 73, "protein": 0.6, "carbohydrates": 17.9, "fat": 0.6, "sugar": 12.0, "fiber": 1.8},
    {"name": "Maracuja", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 97, "protein": 2.2, "carbohydrates": 23.4, "fat": 0.7, "sugar": 11.2, "fiber": 10.4},
    {"name": "Melon", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 34, "protein": 0.8, "carbohydrates": 8.2, "fat": 0.2, "sugar": 7.9, "fiber": 0.9},
    {"name": "Mulberry", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 43, "protein": 1.4, "carbohydrates": 9.8, "fat": 0.4, "sugar": 8.1, "fiber": 1.7},
    {"name": "Nectarine", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 44, "protein": 1.1, "carbohydrates": 10.6, "fat": 0.3, "sugar": 7.9, "fiber": 1.7},
    {"name": "Nut", "category": "Nuts & Seeds", "serving_size": 100, "serving_unit": "g", "calories": 607, "protein": 20.0, "carbohydrates": 21.0, "fat": 53.0, "sugar": 4.0, "fiber": 7.0},
    {"name": "Onion", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 40, "protein": 1.1, "carbohydrates": 9.3, "fat": 0.1, "sugar": 4.2, "fiber": 1.7},
    {"name": "Orange", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 47, "protein": 0.9, "carbohydrates": 11.8, "fat": 0.1, "sugar": 9.4, "fiber": 2.4},
    {"name": "Papaya", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 43, "protein": 0.5, "carbohydrates": 10.8, "fat": 0.3, "sugar": 7.8, "fiber": 1.7},
    {"name": "Passion", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 97, "protein": 2.2, "carbohydrates": 23.4, "fat": 0.7, "sugar": 11.2, "fiber": 10.4},
    {"name": "Peach", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 39, "protein": 0.9, "carbohydrates": 9.5, "fat": 0.3, "sugar": 8.4, "fiber": 1.5},
    {"name": "Pear", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 57, "protein": 0.4, "carbohydrates": 15.2, "fat": 0.1, "sugar": 9.8, "fiber": 3.1},
    {"name": "Pepino", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 26, "protein": 0.4, "carbohydrates": 6.0, "fat": 0.1, "sugar": 4.5, "fiber": 1.0},
    {"name": "Pepper", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 31, "protein": 1.0, "carbohydrates": 6.0, "fat": 0.3, "sugar": 4.2, "fiber": 2.1},
    {"name": "Physalis", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 53, "protein": 1.9, "carbohydrates": 11.2, "fat": 0.7, "sugar": 6.0, "fiber": 4.9},
    {"name": "Pineapple", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 50, "protein": 0.5, "carbohydrates": 13.1, "fat": 0.1, "sugar": 9.9, "fiber": 1.4},
    {"name": "Pistachio", "category": "Nuts & Seeds", "serving_size": 100, "serving_unit": "g", "calories": 562, "protein": 20.2, "carbohydrates": 27.2, "fat": 45.3, "sugar": 7.7, "fiber": 10.6},
    {"name": "Pitahaya", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 57, "protein": 1.1, "carbohydrates": 13.0, "fat": 0.1, "sugar": 7.7, "fiber": 3.0},
    {"name": "Plum", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 46, "protein": 0.7, "carbohydrates": 11.4, "fat": 0.3, "sugar": 9.9, "fiber": 1.4},
    {"name": "Pomegranate", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 83, "protein": 1.7, "carbohydrates": 18.7, "fat": 1.2, "sugar": 13.7, "fiber": 4.0},
    {"name": "Pomelo", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 38, "protein": 0.8, "carbohydrates": 9.6, "fat": 0.0, "sugar": 7.0, "fiber": 1.0},
    {"name": "Potato", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 77, "protein": 2.0, "carbohydrates": 17.5, "fat": 0.1, "sugar": 0.8, "fiber": 2.2},
    {"name": "Quince", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 57, "protein": 0.4, "carbohydrates": 15.3, "fat": 0.1, "sugar": 8.9, "fiber": 1.9},
    {"name": "Rambutan", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 68, "protein": 0.9, "carbohydrates": 16.5, "fat": 0.2, "sugar": 13.0, "fiber": 0.9},
    {"name": "Raspberry", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 52, "protein": 1.2, "carbohydrates": 11.9, "fat": 0.7, "sugar": 4.4, "fiber": 6.5},
    {"name": "Redcurrant", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 56, "protein": 1.4, "carbohydrates": 13.8, "fat": 0.2, "sugar": 7.4, "fiber": 4.3},
    {"name": "Salak", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 82, "protein": 0.8, "carbohydrates": 22.0, "fat": 0.4, "sugar": 14.0, "fiber": 2.6},
    {"name": "Strawberry", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 32, "protein": 0.7, "carbohydrates": 7.7, "fat": 0.3, "sugar": 4.9, "fiber": 2.0},
    {"name": "Tamarillo", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 31, "protein": 1.0, "carbohydrates": 6.0, "fat": 0.4, "sugar": 4.0, "fiber": 3.3},
    {"name": "Tangelo", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 47, "protein": 0.8, "carbohydrates": 11.7, "fat": 0.1, "sugar": 9.0, "fiber": 2.0},
    {"name": "Tomato", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 18, "protein": 0.9, "carbohydrates": 3.9, "fat": 0.2, "sugar": 2.6, "fiber": 1.2},
    {"name": "Walnut", "category": "Nuts & Seeds", "serving_size": 100, "serving_unit": "g", "calories": 654, "protein": 15.2, "carbohydrates": 13.7, "fat": 65.2, "sugar": 2.6, "fiber": 6.7},
    {"name": "Watermelon", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 30, "protein": 0.6, "carbohydrates": 7.6, "fat": 0.2, "sugar": 6.2, "fiber": 0.4},
    {"name": "Zucchini", "category": "Vegetables", "serving_size": 100, "serving_unit": "g", "calories": 17, "protein": 1.2, "carbohydrates": 3.1, "fat": 0.3, "sugar": 2.5, "fiber": 1.0},
    {"name": "Limes", "category": "Fruits", "serving_size": 100, "serving_unit": "g", "calories": 30, "protein": 0.7, "carbohydrates": 10.5, "fat": 0.2, "sugar": 1.7, "fiber": 2.8},
]

def seed_ai_foods():
    db = SessionLocal()

    try:
        added = 0
        skipped = 0

        for food_data in AI_FOODS:

            existing_food = (
                db.query(Food)
                .filter(Food.name.ilike(food_data["name"]))
                .first()
            )

            if existing_food:
                skipped += 1
                continue

            food = Food(**food_data)

            db.add(food)
            added += 1

        db.commit()

        print("\n========================================")
        print("NutriWise AI Food Database")
        print("========================================")
        print(f"Foods added   : {added}")
        print(f"Foods skipped : {skipped}")
        print("========================================\n")

    except Exception as e:
        db.rollback()
        print("Error:", e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_ai_foods()