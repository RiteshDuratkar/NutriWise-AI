from transformers import pipeline
from PIL import Image

print("Loading Indian food model...")

classifier = pipeline(
    "image-classification",
    model="dima806/indian_food_image_detection"
)

print("Indian food model loaded!\n")

image = Image.open("test_biryani.jpg").convert("RGB")

results = classifier(image)

print("Top predictions:")
for result in results[:10]:
    print(
        f"{result['label']}: "
        f"{result['score']:.4f}"
    )