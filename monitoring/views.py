from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Station, Measurement
from django.utils import timezone
from datetime import timedelta
import random  # For demo data

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
    
    # For demo purposes, generate random data
    current_data = {
        'machine_id': station_id,  # Include machine ID in response
        'temperature': round(random.uniform(10, 30), 1),
        'humidity': round(random.uniform(20, 60), 1),
        'pressure': round(random.uniform(15, 20), 1),
        'energy': round(random.uniform(50, 100), 1),
        'vibration': round(random.uniform(0, 100), 1),  # Add vibration data
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
        historical_data.append({
            'machine_id': station_id,  # Include machine ID in historical data
            'timestamp': time.strftime('%Y-%m-%d %H:%M'),
            'temperature': round(random.uniform(10, 30), 1),
            'humidity': round(random.uniform(20, 60), 1),
            'pressure': round(random.uniform(15, 20), 1),
            'energy': round(random.uniform(50, 100), 1),
            'vibration': round(random.uniform(0, 100), 1),  # Add vibration data
        })

    # Sort historical data if requested
    if sort_by == 'machine_id':
        historical_data.sort(key=lambda x: x['machine_id'])
    elif sort_by == 'temperature':
        historical_data.sort(key=lambda x: x['temperature'])
    elif sort_by == 'humidity':
        historical_data.sort(key=lambda x: x['humidity'])
    elif sort_by == 'pressure':
        historical_data.sort(key=lambda x: x['pressure'])
    elif sort_by == 'energy':
        historical_data.sort(key=lambda x: x['energy'])
    elif sort_by == 'vibration':  # Add sorting by vibration
        historical_data.sort(key=lambda x: x['vibration'])
    elif sort_by == 'timestamp':
        historical_data.sort(key=lambda x: x['timestamp'])

    return JsonResponse({
        'current': current_data,
        'historical': historical_data
    })
