from flask import Flask, request, jsonify
import joblib

# Load the trained model
model = joblib.load("models/wine_variety_model.pkl")

# Initialize the Flask app
app = Flask(__name__)

# Define the API endpoint for predicting wine variety
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    reviews = data["reviews"]
    predictions = model.predict(reviews)
    return jsonify({"predictions": predictions.tolist()})

# Run the Flask app
if __name__ == "__main__":
    app.run()
# Run the Flask app