from django.urls import path
from .views import festivais_view, festival_view


app_name = 'festivais'

urlpatterns = [
    path('', festivais_view, name='festivais_view'),
    path('festival/<int:festival_id>', festival_view, name= 'festival_view')
]