from django.http import JsonResponse

def buscar_dados(request):
    dados = {"mensagem": "API funcionando corretamente!"}
    return JsonResponse(dados)
