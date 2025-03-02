from django.urls import path
from .views import criar_filme, listar_filmes, detalhar_filme, atualizar_filme, deletar_filme
from .views import index

urlpatterns = [
    path('', index, name='home'),
    path("filme/criar/", criar_filme, name="criar_filme"),
    path("filme/listar/", listar_filmes, name="listar_filmes"),
    path("filme/detalhar/<int:filme_id>/", detalhar_filme, name="detalhar_filme"),
    path("filme/atualizar/<int:filme_id>/", atualizar_filme, name="atualizar_filme"),
    path("filme/deletar/<int:filme_id>/", deletar_filme, name="deletar_filme"),
]
