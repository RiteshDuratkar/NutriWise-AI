from transformers import pipeline
from PIL import Image
import time

print("Loading food recognition model...")

classifier = pipeline(
    "image-classification",
    model="nateraw/food",
)

print("Food recognition model loaded successfully!")

print("\nOpening food image...")

image = Image.open("test_food.jpg")

print("Running AI recognition...")

start_time = time.time()

results = classifier(image)

end_time = time.time()

print("\nAI Recognition Results:")
print("-" * 40)

for result in results[:5]:
    print(
        f"{result['label']} "
        f"-> confidence: {result['score']:.4f}"
    )

print("-" * 40)

print(
    f"Inference time: {end_time - start_time:.2f} seconds"
)