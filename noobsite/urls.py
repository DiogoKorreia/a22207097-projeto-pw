from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('just/', views.just_view),
    path('nothing/', views.nothing_view),
    path('smile/', views.smile_view),
]