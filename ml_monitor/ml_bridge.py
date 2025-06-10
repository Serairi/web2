import sys
import os
from datetime import datetime
import json

# Add the elastic-faker-pipeline directory to Python path
ELASTIC_FAKER_PATH = "c:/elastic-faker-pipeline"
if ELASTIC_FAKER_PATH not in sys.path:
    sys.path.append(ELASTIC_FAKER_PATH)

# Import the ML components
from predict_anomalies import load_model, predict_anomalies
from generate_test_data import generate_sensor_data

class MLBridge:
    def __init__(self):
        self.model = load_model()
        self.results_file = os.path.join(ELASTIC_FAKER_PATH, "anomaly_results.json")
    
    def get_latest_reading(self):
        """Get the latest sensor reading with anomaly prediction"""
        # Generate new reading
        reading = generate_sensor_data(0)  # ID doesn't matter for single reading
        
        # Get prediction
        data = pd.DataFrame([reading])
        scores, is_anomaly = predict_anomalies(self.model, data)
        
        # Prepare result
        result = {
            "timestamp": reading["timestamp"],
            "energy": reading["energy"],
            "humidity": reading["humidity"],
            "pressure": reading["pressure"],
            "temperature": reading["temperature"],
            "anomaly_score": float(scores[0]),
            "is_anomaly": bool(is_anomaly[0]),
            "machine": "Mounting 2"
        }
        
        # Save result
        with open(self.results_file, 'w') as f:
            json.dump(result, f, indent=4)
        
        return result
    
    def get_latest_anomaly(self):
        """Get the latest anomaly result from the file"""
        try:
            with open(self.results_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return None 