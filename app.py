from flask import Flask, request, jsonify, render_template
from flask.logging import create_logger
import logging
import traceback
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

FEATURE_NAMES = [
    "MedInc", "HouseAge", "AveRooms", "AveBedrms",
    "Population", "AveOccup", "Latitude", "Longitude"
]

def scale(payload):
    LOG.info("Scaling Payload...")
    scaler = StandardScaler().fit(payload)
    return scaler.transform(payload)

@app.route("/", methods = ["GET"])
def home():
    return render_template("form.html", features = FEATURE_NAMES)#"<h3>Sklearn Prediction Home: California Housing Model</h3>"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        clf = joblib.load("california_housing_prediction.joblib")
    except Exception as e:
        LOG.error("Error loading model: %s", str(e))
        LOG.error("Exception traceback: %s", traceback.format_exc())
        return "Model not loaded", 500

    json_payload = request.get_json()
    LOG.info("Received JSON payload: %s", json_payload)

    expected_keys = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
    if not all(key in json_payload for key in expected_keys):
        return jsonify({"error": "Missing one or more input features"}), 400

    input_df = pd.DataFrame([json_payload])
    LOG.info("Inference payload DataFrame:\n%s", input_df)

    scaled_payload = scale(input_df)
    prediction = list(clf.predict(scaled_payload))
    return jsonify({"prediction": prediction})

@app.route("/predict_form", methods=["POST"])
def predict_form():
    try:
        # Parse input values
        input_data = [float(request.form[f]) for f in FEATURE_NAMES]
        input_df = pd.DataFrame([input_data], columns=FEATURE_NAMES)

        # Load model and make prediction
        model = joblib.load("california_housing_prediction.joblib")
        scaled_input = StandardScaler().fit(input_df).transform(input_df)
        prediction = model.predict(scaled_input)

        return f"<h3>Predicted Median House Value: {prediction[0]:.2f}</h3><a href='/'>Try again</a>"

    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

