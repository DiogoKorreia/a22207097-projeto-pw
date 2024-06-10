from django.urls import path
from .views import lisbonToday_view, weather_view, api_view

app_name = 'meteo'

urlpatterns = [
    path('lisbonToday/', lisbonToday_view, name='lisbon_view'),
    path('weather/', weather_view, name='weather_view'),
    path('api/',api_view,name='api_view')
]