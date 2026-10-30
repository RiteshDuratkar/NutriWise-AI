import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image
from huggingface_hub import hf_hub_download
import json


print("Loading fruit recognition model...")


# Download model configuration
config_path = hf_hub_download(
    repo_id="bhumong/fruit-classifier-efficientnet-b0",
    filename="config.json"
)

with open(config_path, "r") as f:
    config = json.load(f)


# Create EfficientNet-B0
model = models.efficientnet_b0(weights=None)

num_labels = config["num_labels"]

num_ftrs = model.classifier[1].in_features

model.classifier[1] = torch.nn.Linear(
    num_ftrs,
    num_labels
)


# Download trained weights
model_path = hf_hub_download(
    repo_id="bhumong/fruit-classifier-efficientnet-b0",
    filename="pytorch_model.bin"
)


# Load weights
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

state_dict = torch.load(
    model_path,
    map_location=device
)

model.load_state_dict(state_dict)

model.to(device)
model.eval()


print("Model loaded successfully.")


# Image preprocessing
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# Load test image
image = Image.open("test_apple.jpg").convert("RGB")

input_tensor = preprocess(image)

input_batch = input_tensor.unsqueeze(0).to(device)


# Prediction
with torch.no_grad():
    output = model(input_batch)

probabilities = torch.nn.functional.softmax(
    output,
    dim=1
)[0]


top_probabilities, top_indices = torch.topk(
    probabilities,
    5
)


print("\nFruit AI predictions:")

for probability, index in zip(
    top_probabilities,
    top_indices
):
    label = config["id2label"][str(index.item())]

    print(
        label,
        round(probability.item(), 4)
    )