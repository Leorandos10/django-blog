import requests
from django.conf import settings

OMDB_API_KEY = "5de57a3a"
OMDB_URL = "http://www.omdbapi.com/"

def buscar_filme_omdb(titulo):
    """Busca um filme na API OMDb pelo título."""
    params = {
        "t": titulo,
        "apikey": OMDB_API_KEY
    }
    
    response = requests.get(OMDB_URL, params=params)
    
    if response.status_code == 200:
        dados = response.json()
        if dados.get("Response") == "True":
            return {
                "titulo": dados.get("Title"),
                "ano": dados.get("Year"),
                "diretor": dados.get("Director"),
                "imdb_id": dados.get("imdbID"),
            }
    return None
