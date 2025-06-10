import joblib
import numpy as np
import os

def predict_anomalies(model, data):
    """
    Predict anomalies in sensor data using the trained model.
    
    Parameters:
    - model: Trained IsolationForest model
    - data: pandas DataFrame containing sensor readings
    
    Returns:
    - Tuple of (anomaly_scores, is_anomaly)
    """
    try:
        # Extract only the numerical features
        features = data[["temperature", "humidity", "pressure", "energy", "vibration"]]
        
        # Get anomaly scores (-1 for anomalies, 1 for normal)
        predictions = model.predict(features)
        
        # Get decision function scores (lower = more anomalous)
        scores = model.score_samples(features)
        
        # Convert predictions to boolean (True for anomalies)
        is_anomaly = predictions == -1
        
        return scores, is_anomaly
    except Exception as e:
        print(f"Error in predict_anomalies: {str(e)}")
        # Return default values in case of error
        return np.zeros(len(data)), np.zeros(len(data), dtype=bool)

def load_model(filename='isolation_forest_model.joblib'):
    """
    Load the trained model from file.
    
    Parameters:
    - filename: Path to the model file
    
    Returns:
    - Loaded model
    """
    model_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(model_dir, filename)
    
    try:
        print(f"Loading model from {model_path}...")
        return joblib.load(model_path)
    except FileNotFoundError:
        raise FileNotFoundError("Model file not found. Please train the model first.")
