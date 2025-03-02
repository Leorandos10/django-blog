from django.urls import path, include

urlpatterns = [
    path("api/", include("meu_app.urls")),
]
