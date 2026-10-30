import requests

url = "http://127.0.0.1:8000/ai/analyze-food"

with open("test_biryani.jpg", "rb") as image:
    response = requests.post(
        url,
        files={
            "file": (
                "test_biryani.jpg",
                image,
                "image/jpeg"
            )
        }
    )

print("Status code:", response.status_code)

print("\nResponse:")
print(response.json())