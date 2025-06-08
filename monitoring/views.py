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

def get_station_data(request):
    station_id = request.GET.get('station', 1)
    time_range = request.GET.get('range', '7days')
    
    # For demo purposes, generate random data
    current_data = {
        'temperature': round(random.uniform(10, 30), 1),
        'humidity': round(random.uniform(20, 60), 1),
        'pressure': round(random.uniform(15, 20), 1),
        'energy': round(random.uniform(50, 100), 1),
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
            'timestamp': time.strftime('%Y-%m-%d %H:%M'),
            'temperature': round(random.uniform(10, 30), 1),
            'humidity': round(random.uniform(20, 60), 1),
            'pressure': round(random.uniform(15, 20), 1),
            'energy': round(random.uniform(50, 100), 1),
        })

    return JsonResponse({
        'current': current_data,
        'historical': historical_data
    })
