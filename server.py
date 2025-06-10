from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
from datetime import datetime, timedelta
import random
import sys
import os

# Add the elastic-faker-pipeline directory to Python path
ELASTIC_FAKER_PATH = "c:/elastic-faker-pipeline"
if ELASTIC_FAKER_PATH not in sys.path:
    sys.path.append(ELASTIC_FAKER_PATH)

# Import ML components
from predict_anomalies import load_model, predict_anomalies
from generate_test_data import generate_sensor_data
import pandas as pd

class DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Load the ML model when server starts
        self.model = load_model()
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        if self.path == '/api/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Generate new reading using the ML generator
            reading = generate_sensor_data(0)  # ID doesn't matter for single reading
            
            # Get prediction
            data = pd.DataFrame([reading])
            scores, is_anomaly = predict_anomalies(self.model, data)
            
            # Prepare response data
            response_data = {
                'temperature': reading["temperature"],
                'humidity': reading["humidity"],
                'pressure': reading["pressure"],
                'energy': reading["energy"],
                'timeLabels': [(datetime.now() - timedelta(hours=x)).strftime('%H:%M') for x in range(6)],
                'temperatureHistory': [random.uniform(10, 30) for _ in range(6)],
                'humidityHistory': [random.uniform(20, 60) for _ in range(6)],
                'is_anomaly': bool(is_anomaly[0]),
                'anomaly_score': float(scores[0]),
                'machine': "Mounting 2",
                'sensor': self._get_anomalous_sensor(reading) if bool(is_anomaly[0]) else None
            }
            
            self.wfile.write(json.dumps(response_data).encode())
            return
            
        return SimpleHTTPRequestHandler.do_GET(self)
    
    def _get_anomalous_sensor(self, reading):
        """Determine which sensor is showing anomalous behavior"""
        thresholds = {
            'Temperature': {'min': 18, 'max': 26},
            'Humidity': {'min': 30, 'max': 70},
            'Pressure': {'min': 970, 'max': 1030},
            'Energy': {'min': 600, 'max': 800}
        }
        
        if reading['temperature'] < thresholds['Temperature']['min'] or reading['temperature'] > thresholds['Temperature']['max']:
            return 'Temperature'
        elif reading['humidity'] < thresholds['Humidity']['min'] or reading['humidity'] > thresholds['Humidity']['max']:
            return 'Humidity'
        elif reading['pressure'] < thresholds['Pressure']['min'] or reading['pressure'] > thresholds['Pressure']['max']:
            return 'Pressure'
        elif reading['energy'] < thresholds['Energy']['min'] or reading['energy'] > thresholds['Energy']['max']:
            return 'Energy'
        return None

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, DashboardHandler)
    print('Server running on http://localhost:8000')
    httpd.serve_forever() 