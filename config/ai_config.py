# AI Model Configuration
AI_MODEL_PATH = "models/anomaly_detection.pkl"  # Pre-trained model
AI_TRAINING_DATA_PATH = "data/behavior_tracking.json"

# Feature Selection for Behavioral Analysis
FEATURES = ["login_frequency", "movement_patterns", "transaction_history", "interaction_timeline"]

# Machine Learning Model Parameters
MODEL_HYPERPARAMETERS = {
    "max_depth": 5,
    "n_estimators": 100,
    "random_state": 42
}

# Anomaly Detection Threshold
ANOMALY_THRESHOLD = 0.2  # Lower means stricter fraud detection

# AI Logging
ENABLE_AI_LOGGING = True
