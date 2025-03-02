from django.urls import path
from .views import buscar_filme

urlpatterns = [
    path('filme/', buscar_filme, name='buscar_filme'),
]
