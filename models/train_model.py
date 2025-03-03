#This script trains an anomaly detection model (e.g., Isolation Forest or Random Forest) using historical user behavior data.
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

# Load Dataset (Behavioral Tracking Data)
DATA_PATH = "data/behavior_tracking.json"

try:
    df = pd.read_json(DATA_PATH)
    print("Data Loaded Successfully")
except Exception as e:
    print(f"Error Loading Data: {e}")
    df = None

if df is not None:
    # Select behavioral features
    FEATURES = ["login_frequency", "movement_patterns", "transaction_history", "interaction_timeline"]

    X = df[FEATURES]

    # Train an Isolation Forest for Anomaly Detection
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(X)

    # Save the trained model
    joblib.dump(model, "models/model_weights.pkl")
    print("✅ Anomaly Detection Model Trained & Saved Successfully")
