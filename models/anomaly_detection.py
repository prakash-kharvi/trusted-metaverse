#This script loads a pre-trained anomaly detection model to evaluate user behavior consistency.
import joblib
import numpy as np

# Load the pre-trained model
MODEL_PATH = "models/model_weights.pkl"

try:
    anomaly_model = joblib.load(MODEL_PATH)
    print("AI Model Loaded Successfully")
except Exception as e:
    print(f"Error Loading AI Model: {e}")
    anomaly_model = None


def detect_anomalies(user_features):
    """
    Detects anomalies in user behavior using a trained machine learning model.

    Parameters:
        user_features (list): List of behavioral feature values (e.g., login frequency, interactions).

    Returns:
        anomaly_score (float): A value from 0 to 1 (higher = more likely fraudulent).
    """
    if anomaly_model is None:
        return 0.5  # Default to neutral score if model is unavailable

    # Convert features into a numpy array
    user_features = np.array(user_features).reshape(1, -1)

    # Predict anomaly score
    anomaly_score = anomaly_model.predict_proba(user_features)[:, 1][0]  # Probability of fraud

    return round(anomaly_score, 2)
