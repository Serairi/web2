from django.urls import path
from . import views

app_name = 'monitoring'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('api/station-data/', views.get_station_data, name='station_data'),
    path('api/stations/', views.get_stations, name='stations'),
] 