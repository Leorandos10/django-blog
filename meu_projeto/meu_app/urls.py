from django.urls import path
from . import views  # Importa o views corretamente

urlpatterns = [
    path('buscar/', views.buscar_dados, name='buscar_dados'),  # Certifique-se de que 'buscar_dados' existe no views.py
]
