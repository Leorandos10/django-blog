import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import Filme
from django.conf import settings


# Criar um filme (Create)
@csrf_exempt
def criar_filme(request):
    if request.method == "POST":
        data = json.loads(request.body)
        titulo = data.get("titulo")

        if not titulo:
            return JsonResponse({"erro": "Informe um título de filme."}, status=400)

        url = f"http://www.omdbapi.com/?t={titulo}&apikey={settings.OMDB_API_KEY}"
        response = requests.get(url)
        filme_data = response.json()

        if filme_data.get("Response") == "False":
            return JsonResponse({"erro": "Filme não encontrado."}, status=404)

        filme = Filme.objects.create(
            titulo=filme_data["Title"],
            ano=filme_data["Year"],
            diretor=filme_data.get("Director"),
            genero=filme_data.get("Genre"),
            imdb_id=filme_data["imdbID"],
        )

        return JsonResponse({"mensagem": "Filme salvo!", "id": filme.id}, status=201)


# Listar todos os filmes (Read)
def listar_filmes(request):
    filmes = Filme.objects.all().values()
    return JsonResponse(list(filmes), safe=False)


# Atualizar um filme (Update)
@csrf_exempt
def atualizar_filme(request, imdb_id):
    filme = get_object_or_404(Filme, imdb_id=imdb_id)

    if request.method == "PUT":
        data = json.loads(request.body)
        filme.titulo = data.get("titulo", filme.titulo)
        filme.ano = data.get("ano", filme.ano)
        filme.diretor = data.get("diretor", filme.diretor)
        filme.genero = data.get("genero", filme.genero)
        filme.save()

        return JsonResponse({"mensagem": "Filme atualizado!"})


# Excluir um filme (Delete)
@csrf_exempt
def deletar_filme(request, imdb_id):
    filme = get_object_or_404(Filme, imdb_id=imdb_id)

    if request.method == "DELETE":
        filme.delete()
        return JsonResponse({"mensagem": "Filme deletado!"})
