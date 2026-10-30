from transformers import pipeline

print("Loading food recognition model...")

classifier = pipeline(
    "image-classification",
    model="nateraw/food",
)

print("Food recognition model loaded successfully!")