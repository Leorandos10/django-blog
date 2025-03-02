import requests
from django.http import JsonResponse
from django.conf import settings

def buscar_filme(request):
    titulo = request.GET.get("titulo", "").strip()
    if not titulo:
        return JsonResponse({"erro": "Informe um título de filme."}, status=400)

    api_key = settings.OMDB_API_KEY
    if not api_key:
        return JsonResponse({"erro": "API Key não encontrada no Django."}, status=500)

    url = f"http://www.omdbapi.com/?t={titulo}&apikey={api_key}"
    print(f"URL gerada: {url}")  # Verifique se a URL está correta

    resposta = requests.get(url)
    print(f"Status Code: {resposta.status_code}")  # Deve ser 200
    print(f"Resposta JSON: {resposta.text}")  # Veja a resposta da API

    if resposta.status_code == 200:
        return JsonResponse(resposta.json(), safe=False)
    else:
        return JsonResponse({"erro": "Falha ao buscar filme."}, status=500)
