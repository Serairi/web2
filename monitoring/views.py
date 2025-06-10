from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Station, Measurement
from django.utils import timezone
from datetime import timedelta
import random  # For demo data
import sys
import os
import pandas as pd

# Add the elastic-faker-pipeline directory to Python path
ELASTIC_FAKER_PATH = "c:/elastic-faker-pipeline"
if ELASTIC_FAKER_PATH not in sys.path:
    sys.path.append(ELASTIC_FAKER_PATH)

# Import ML components
from predict_anomalies import load_model, predict_anomalies
from generate_test_data import generate_sensor_data
from train_model import train_isolation_forest

# Try to load the model, if not found, train it first
try:
    ml_model = load_model()
except FileNotFoundError:
    print("Model not found, training new model...")
    # Generate some initial data for training
    training_data = []
    for _ in range(1000):  # Generate 1000 samples for training
        reading = generate_sensor_data(0)
        training_data.append(reading)
    
    # Convert to DataFrame
    df = pd.DataFrame(training_data)
    
    # Train the model
    ml_model = train_isolation_forest(df)
    print("Model training completed!")

class DashboardView(TemplateView):
    template_name = 'monitoring/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stations'] = Station.objects.all()
        return context

def get_stations(request):
    """API endpoint to get list of all stations"""
    stations = list(Station.objects.values('id', 'name', 'description'))
    return JsonResponse({'stations': stations})

def get_station_data(request):
    station_id = request.GET.get('station', 1)
    time_range = request.GET.get('range', '7days')
    sort_by = request.GET.get('sort', 'id')  # Default sort by ID
    
    # Generate data using ML generator
    reading = generate_sensor_data(0)  # ID doesn't matter for single reading
    
    # Get prediction
    data = pd.DataFrame([reading])
    scores, is_anomaly = predict_anomalies(ml_model, data)
    
    # Determine which sensor is anomalous
    anomalous_sensor = None
    if is_anomaly[0]:
        thresholds = {
            'Temperature': {'min': 18, 'max': 26},
            'Humidity': {'min': 30, 'max': 70},
            'Pressure': {'min': 970, 'max': 1030},
            'Energy': {'min': 600, 'max': 800}
        }
        
        if reading['temperature'] < thresholds['Temperature']['min'] or reading['temperature'] > thresholds['Temperature']['max']:
            anomalous_sensor = 'Temperature'
        elif reading['humidity'] < thresholds['Humidity']['min'] or reading['humidity'] > thresholds['Humidity']['max']:
            anomalous_sensor = 'Humidity'
        elif reading['pressure'] < thresholds['Pressure']['min'] or reading['pressure'] > thresholds['Pressure']['max']:
            anomalous_sensor = 'Pressure'
        elif reading['energy'] < thresholds['Energy']['min'] or reading['energy'] > thresholds['Energy']['max']:
            anomalous_sensor = 'Energy'
    
    # Prepare current data with ML predictions
    current_data = {
        'machine_id': station_id,
        'temperature': reading['temperature'],
        'humidity': reading['humidity'],
        'pressure': reading['pressure'],
        'energy': reading['energy'],
        'is_anomaly': bool(is_anomaly[0]),
        'anomaly_score': float(scores[0]),
        'machine': "Mounting 2",
        'sensor': anomalous_sensor
    }
    
    # Generate historical data
    now = timezone.now()
    if time_range == '7days':
        start_time = now - timedelta(days=7)
        interval = timedelta(days=1)
        points = 7
    elif time_range == '24hours':
        start_time = now - timedelta(hours=24)
        interval = timedelta(hours=4)
        points = 6
    else:
        start_time = now - timedelta(hours=1)
        interval = timedelta(minutes=10)
        points = 6

    historical_data = []
    for i in range(points):
        time = start_time + (interval * i)
        reading = generate_sensor_data(i)
        historical_data.append({
            'machine_id': station_id,
            'timestamp': time.strftime('%Y-%m-%d %H:%M'),
            'temperature': reading['temperature'],
            'humidity': reading['humidity'],
            'pressure': reading['pressure'],
            'energy': reading['energy']
        })

    # Sort historical data if requested
    if sort_by in ['machine_id', 'temperature', 'humidity', 'pressure', 'energy', 'timestamp']:
        historical_data.sort(key=lambda x: x[sort_by])

    return JsonResponse({
        'current': current_data,
        'historical': historical_data
    })
