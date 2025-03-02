"""
URL configuration for meu_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from meu_app.views import criar_filme, listar_filmes, atualizar_filme, deletar_filme


urlpatterns = [
    path("filme/", criar_filme, name="criar_filme"),
    path("filmes/", listar_filmes, name="listar_filmes"),
    path("filme/<str:imdb_id>/", atualizar_filme, name="atualizar_filme"),
    path("filme/<str:imdb_id>/delete/", deletar_filme, name="deletar_filme"),
]

def home(request):
    return HttpResponse(
        "Página inicial funcionando! \nPesquise por: http://127.0.0.1:8000/api/filme/?titulo=Dune"
    )
