import os

from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException, File, UploadFile

# Load environment variables from .env
load_dotenv()
from database.database import SessionLocal



# AI model imports
from transformers import pipeline
from PIL import Image

from database.database import Base, engine
from models.user import User
from models.profile import Profile
from models.goal import Goal
from models.food import Food
from models.food_history import FoodHistory
from models.water_intake import WaterIntake
from models.meal_plan import MealPlan

from routers.user import router as user_router
from routers.auth import router as auth_router
from routers.food import router as food_router
from routers.food_history import router as food_history_router
from routers.goal import router as goal_router
from routers.meal_plan import router as meal_plan_router
from routers.water_intake import router as water_intake_router


Base.metadata.create_all(bind=engine)


app = FastAPI()


# ============================================================
# CORS CONFIGURATION
# ============================================================

frontend_url = os.getenv(
    "FRONTEND_URL",
    "http://localhost:5173"
)

allowed_origins = [
    "http://localhost:5173"
]

if frontend_url and frontend_url not in allowed_origins:
    allowed_origins.append(frontend_url)


app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# AI FOOD RECOGNITION MODEL
# ============================================================

print("Loading food recognition AI model...")

food_classifier = pipeline(
    "image-classification",
    model="nateraw/food",
)

indian_food_classifier = pipeline(
    "image-classification",
    model="dima806/indian_food_image_detection",
)

# Fruit AI model
import torch
import torchvision.models as models
from torchvision import transforms
from huggingface_hub import hf_hub_download
import json

fruit_config_path = hf_hub_download(
    repo_id="bhumong/fruit-classifier-efficientnet-b0",
    filename="config.json"
)

with open(fruit_config_path, "r") as f:
    fruit_config = json.load(f)

fruit_classifier = models.efficientnet_b0(weights=None)

num_labels = fruit_config["num_labels"]

num_ftrs = fruit_classifier.classifier[1].in_features

fruit_classifier.classifier[1] = torch.nn.Linear(
    num_ftrs,
    num_labels
)

fruit_model_path = hf_hub_download(
    repo_id="bhumong/fruit-classifier-efficientnet-b0",
    filename="pytorch_model.bin"
)

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

fruit_classifier.load_state_dict(
    torch.load(
        fruit_model_path,
        map_location=device
    )
)

fruit_classifier.to(device)
fruit_classifier.eval()

fruit_preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

print("Food recognition AI models loaded successfully!")

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(food_router)
app.include_router(food_history_router)
app.include_router(goal_router)
app.include_router(meal_plan_router)
app.include_router(water_intake_router)


@app.get("/")
def home():
    return {"message": "NutriWise Backend is running!"}

@app.post("/ai/analyze-food")
async def analyze_food_image(file: UploadFile = File(...)):
    db = SessionLocal()

    try:
        # Read uploaded image
        image_bytes = await file.read()

        # Open image using PIL
        from io import BytesIO

        image = Image.open(BytesIO(image_bytes)).convert("RGB")

        # Run AI food recognition
        general_results = food_classifier(image)
        indian_results = indian_food_classifier(image)

        # Run Fruit AI
        fruit_input = fruit_preprocess(image).unsqueeze(0).to(device)

        with torch.no_grad():
            fruit_output = fruit_classifier(fruit_input)

        fruit_probabilities = torch.nn.functional.softmax(
            fruit_output,
            dim=1
        )[0]

        fruit_top_probabilities, fruit_top_indices = torch.topk(
            fruit_probabilities,
            5
        )

        fruit_results = []

        for probability, index in zip(
            fruit_top_probabilities,
            fruit_top_indices
        ):
            label = fruit_config["id2label"][str(index.item())]

            fruit_results.append({
                "label": label,
                "score": probability.item()
            })

        print("\nFruit AI:")
        for result in fruit_results[:5]:
            print(
                result["label"],
                round(result["score"], 4)
            )
        

        print("\nGeneral AI:")
        for result in general_results[:5]:
            print(result["label"], round(result["score"], 4))

        print("\nIndian AI:")
        for result in indian_results[:5]:
            print(result["label"], round(result["score"], 4))

                # Find predictions that exist in our food database
        general_food = None
        indian_food = None
        fruit_food = None

        for result in general_results[:5]:
            food = (
                db.query(Food)
                .filter(Food.name.ilike(result["label"]))
                .first()
            )
            if food:
                general_food = (result, food)
                break

        # Find Indian AI predictions that exist in our food database
        for result in indian_results[:5]:
            food_name = result["label"].replace("_", " ")

            food = (
                db.query(Food)
                .filter(Food.name.ilike(food_name))
                .first()
            )

            if food:
                indian_food = (result, food)
                break

        # Find Fruit AI predictions that exist in our food database
        for result in fruit_results[:5]:
            food_name = result["label"].replace("_", " ")

            food = (
                db.query(Food)
                .filter(Food.name.ilike(food_name))
                .first()
            )

            if food:
                fruit_food = (result, food)
                break

        # Select a database-matched prediction.
        #
        # General AI has priority when it finds a database match.
        # Otherwise use Indian AI, then Fruit AI.
        # If no AI prediction matches the database, fall back
        # to the General AI prediction.

        if general_food:
            top_result, food = general_food
            detected_food = food.name
            confidence = top_result["score"]
            detection_source = "general"

        elif indian_food:
            top_result, food = indian_food
            detected_food = food.name
            confidence = top_result["score"]
            detection_source = "indian"

        elif fruit_food:
            top_result, food = fruit_food
            detected_food = food.name
            confidence = top_result["score"]
            detection_source = "fruit"

        else:
            top_result = general_results[0]
            detected_food = top_result["label"]
            confidence = top_result["score"]
            detection_source = "general"
            food = None

        results = (
            indian_results
            if detection_source == "indian"
            else fruit_results
            if detection_source == "fruit"
            else general_results
        )

        # Classify AI confidence level
        if confidence >= 0.70:
            confidence_level = "high"
        elif confidence >= 0.30:
            confidence_level = "medium"
        elif confidence >= 0.10:
            confidence_level = "low"
        else:
            confidence_level = "very_low"

        # Search nutrition database only when AI found a database match
        if detection_source == "general" and general_food:
            food = general_food[1]

        elif detection_source == "indian" and indian_food:
            food = indian_food[1]

        elif detection_source == "fruit" and fruit_food:
            food = fruit_food[1]

        else:
            food = None

        return {
            "success": True,
            "food": detected_food,
            "confidence": round(confidence, 4),
            "confidence_level": confidence_level,
            "requires_confirmation": confidence_level in ["low", "very_low"],

            "nutrition": (
                {
                    "id": food.id,
                    "name": food.name,
                    "category": food.category,
                    "serving_size": food.serving_size,
                    "serving_unit": food.serving_unit,
                    "calories": food.calories,
                    "protein": food.protein,
                    "carbohydrates": food.carbohydrates,
                    "fat": food.fat,
                    "sugar": food.sugar,
                    "fiber": food.fiber,
                }
                if food else None
            ),

            "predictions": [
                {
                    "food": result["label"].replace("_", " "),
                    "confidence": round(result["score"], 4)
                }
                for result in (
                    indian_results
                    if detection_source == "indian"
                    else fruit_results
                    if detection_source == "fruit"
                    else general_results
                )[:5]
            ]
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

    finally:
        db.close()