import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
from datetime import datetime
import os

class AnomalyDetector:
    def __init__(self):
        self.model = None
        self.model_path = os.path.join(os.path.dirname(__file__), 'isolation_forest_model.joblib')
    
    def train(self, data):
        """Train the Isolation Forest model"""
        print("Training Isolation Forest model...")
        
        # Select features for training
        features = data[["energy", "humidity", "pressure", "temperature"]]
        
        # Initialize and train the model
        self.model = IsolationForest(
            n_estimators=100,
            contamination=0.1,  # Expected proportion of anomalies
            random_state=42
        )
        
        # Fit the model
        self.model.fit(features)
        
        # Save the model
        self.save_model()
        
        return self.model

    def predict(self, data):
        """Predict anomalies in the data"""
        if self.model is None:
            self.load_model()
            
        if isinstance(data, dict):
            # Convert single reading to DataFrame
            data = pd.DataFrame([data])
            
        features = data[["energy", "humidity", "pressure", "temperature"]]
        
        # Get predictions and scores
        predictions = self.model.predict(features)
        scores = self.model.score_samples(features)
        
        # Prepare results
        results = []
        for idx, row in data.iterrows():
            result = {
                "timestamp": row.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                "energy": row["energy"],
                "humidity": row["humidity"],
                "pressure": row["pressure"],
                "temperature": row["temperature"],
                "anomaly_score": float(scores[idx]),
                "is_anomaly": bool(predictions[idx] == -1)
            }
            if "id" in row:
                result["original_id"] = row["id"]
            results.append(result)
            
        return results[0] if isinstance(data, dict) else results

    def save_model(self):
        """Save the trained model"""
        if self.model is not None:
            joblib.dump(self.model, self.model_path)
            print(f"Model saved to {self.model_path}")

    def load_model(self):
        """Load the trained model"""
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print(f"Model loaded from {self.model_path}")
        else:
            raise FileNotFoundError("No trained model found. Please train the model first.") 