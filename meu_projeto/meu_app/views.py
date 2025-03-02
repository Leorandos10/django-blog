from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Filme
import json


def index(request):
    return render(request, "meu_app/index.html")


@csrf_exempt
def criar_filme(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            titulo = data.get("titulo")
            ano = data.get("ano")
            genero = data.get("genero")

            if not titulo or not ano or not genero:
                return JsonResponse(
                    {"erro": "Todos os campos são obrigatórios."}, status=400
                )

            # Salva no banco de dados real
            filme = Filme.objects.create(titulo=titulo, ano=ano, genero=genero)

            return JsonResponse(
                {"mensagem": "Filme criado com sucesso!", "id": filme.id}, status=201
            )

        except json.JSONDecodeError:
            return JsonResponse({"erro": "JSON inválido."}, status=400)

    return JsonResponse({"erro": "Método não permitido."}, status=405)


import requests
from django.http import JsonResponse
from django.conf import settings

@csrf_exempt
def listar_filmes(request):
    if request.method == "GET":
        # Pega o parâmetro "titulo" da query string, se existir
        titulo = request.GET.get('titulo', None)

        if titulo:
            # Aqui você deve substituir 'sua-chave-de-api' pela chave da API OMDb
            api_key = "5de57a3a"  # Substitua pela sua chave da API
            url = f"http://www.omdbapi.com/?t={titulo}&apikey={api_key}"

            try:
                # Fazendo a solicitação para a API do OMDb
                response = requests.get(url)
                data = response.json()

                if data.get("Response") == "True":
                    return JsonResponse(data)
                else:
                    return JsonResponse({"erro": "Filme não encontrado."}, status=404)

            except requests.exceptions.RequestException as e:
                return JsonResponse({"erro": f"Erro na solicitação: {str(e)}"}, status=500)
        else:
            return JsonResponse({"erro": "Parâmetro 'titulo' é obrigatório."}, status=400)

    return JsonResponse({"erro": "Método não permitido."}, status=405)

@csrf_exempt
def detalhar_filme(request, filme_id):
    try:
        filme = Filme.objects.get(id=filme_id)
        return JsonResponse(
            {
                "id": filme.id,
                "titulo": filme.titulo,
                "ano": filme.ano,
                "genero": filme.genero,
            }
        )
    except Filme.DoesNotExist:
        return JsonResponse({"erro": "Filme não encontrado."}, status=404)


@csrf_exempt
def atualizar_filme(request, filme_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            filme = Filme.objects.get(id=filme_id)

            filme.titulo = data.get("titulo", filme.titulo)
            filme.ano = data.get("ano", filme.ano)
            filme.genero = data.get("genero", filme.genero)
            filme.save()

            return JsonResponse(
                {
                    "mensagem": "Filme atualizado com sucesso!",
                    "filme": {
                        "id": filme.id,
                        "titulo": filme.titulo,
                        "ano": filme.ano,
                        "genero": filme.genero,
                    },
                },
                status=200,
            )

        except Filme.DoesNotExist:
            return JsonResponse({"erro": "Filme não encontrado."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"erro": "JSON inválido."}, status=400)

    return JsonResponse({"erro": "Método não permitido."}, status=405)


@csrf_exempt
def deletar_filme(request, filme_id):
    if request.method == "DELETE":
        try:
            filme = Filme.objects.get(id=filme_id)
            filme.delete()
            return JsonResponse({"mensagem": "Filme deletado com sucesso!"}, status=200)

        except Filme.DoesNotExist:
            return JsonResponse({"erro": "Filme não encontrado."}, status=404)

    return JsonResponse({"erro": "Método não permitido."}, status=405)
