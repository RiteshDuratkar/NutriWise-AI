from PIL import Image
import torch
import json
from torchvision import models, transforms
from huggingface_hub import hf_hub_download


image = Image.open("test_banana1.jpg").convert("RGB")


config_path = hf_hub_download(
    repo_id="bhumong/fruit-classifier-efficientnet-b0",
    filename="config.json"
)

with open(config_path, "r") as f:
    config = json.load(f)


model = models.efficientnet_b0(weights=None)

model.classifier[1] = torch.nn.Linear(
    model.classifier[1].in_features,
    config["num_labels"]
)


model_path = hf_hub_download(
    repo_id="bhumong/fruit-classifier-efficientnet-b0",
    filename="pytorch_model.bin"
)


device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


model.load_state_dict(
    torch.load(
        model_path,
        map_location=device
    )
)

model.to(device)
model.eval()


preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
    )
])


image_tensor = preprocess(image).unsqueeze(0).to(device)


with torch.no_grad():
    output = model(image_tensor)
    probabilities = torch.softmax(output, dim=1)[0]

    values, indices = torch.topk(
        probabilities,
        5
    )


print("\nFruit AI — Banana 2")
print("====================")

for value, index in zip(values, indices):

    label = config["id2label"][str(index.item())]

    print(
        f"{label}: {value.item():.4f}"
    )