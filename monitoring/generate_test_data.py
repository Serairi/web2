import random
from datetime import datetime

def generate_sensor_data(seed=None):
    """
    Generate realistic sensor data for a manufacturing environment.
    
    Parameters:
    - seed: Optional seed for reproducibility
    
    Returns:
    - Dictionary containing sensor readings
    """
    if seed is not None:
        random.seed(seed)
    
    # Base values for each sensor (matching your ranges)
    temperature = round(random.uniform(18.0, 26.0), 2)
    humidity = round(random.uniform(30.0, 70.0), 2)
    pressure = round(random.uniform(970.0, 1000.0), 2)
    energy = round(random.uniform(600.0, 800.0), 2)
    vibration = round(random.uniform(10.0, 50.0), 2)  # Normal range for industrial machinery
    
    return {
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'energy': energy,
        'vibration': vibration,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == '__main__':
    # Example usage
    print(generate_sensor_data())
