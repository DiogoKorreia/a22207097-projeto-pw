from django.urls import path
from . import views

app_name = 'novaapp'

urlpatterns = [
    path('latim/', views.latim_view, name='latim'),
    path('maislatim/', views.maislatim_view, name='maislatim'),
    path('aindamaislatim/', views.aindamaislatim_view, name='aindamaislatim'),
]