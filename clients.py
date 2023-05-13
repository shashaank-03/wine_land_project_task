import requests
import json

# Define the API endpoint URL
url = "http://127.0.0.1:5000/predict/"

# Prepare the request data
data = {
    "reviews": [
        "This wine has a rich and fruity aroma.",
        "I can taste the hints of oak and vanilla in this red wine."
    ]
}

# Send the POST request
response = requests.post(url, json=data)

# Get the predictions from the response
predictions = response.json()["predictions"]

# Print the predictions
print(predictions)
