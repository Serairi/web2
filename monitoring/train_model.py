from sklearn.ensemble import IsolationForest
import joblib
import os

def train_isolation_forest(data, contamination=0.1):
    """
    Train an Isolation Forest model for anomaly detection.
    
    Parameters:
    - data: pandas DataFrame containing sensor readings
    - contamination: The proportion of outliers in the data set (default=0.1)
    
    Returns:
    - Trained IsolationForest model
    """
    # Initialize the model
    model = IsolationForest(
        n_estimators=100,
        contamination=contamination,
        random_state=42
    )
    
    # Train the model
    model.fit(data)
    
    # Save the model
    model_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(model_dir, 'isolation_forest_model.joblib')
    joblib.dump(model, model_path)
    
    return model

def load_model():
    """
    Load the trained Isolation Forest model.
    
    Returns:
    - Loaded IsolationForest model
    """
    model_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(model_dir, 'isolation_forest_model.joblib')
    
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not found. Train the model first.")
    
    return joblib.load(model_path)

if __name__ == '__main__':
    # Example usage
    import pandas as pd
    import numpy as np
    
    # Generate sample data
    np.random.seed(42)
    n_samples = 1000
    data = pd.DataFrame({
        'temperature': np.random.uniform(18, 26, n_samples),
        'humidity': np.random.uniform(30, 70, n_samples),
        'pressure': np.random.uniform(970, 1000, n_samples),
        'energy': np.random.uniform(600, 800, n_samples),
        'vibration': np.random.uniform(10, 50, n_samples)
    })
    
    # Train the model
    model = train_isolation_forest(data)
    print("Model trained and saved successfully!")
