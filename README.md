# Meu Projeto Django

Este é um projeto Django simples que implementa um sistema CRUD com autenticação por tokens e consumo de API externa.

## Requisitos

- Python 3.10+
- Django
- Django REST Framework
- Docker & Docker Compose
- Git
- MySQL ou PostgreSQL

1- criar um filme POST
	Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/criar/" -Method POST -ContentType "application/json" -Body '{"titulo": "John Wick", "ano": 2014, "genero": "Action"}'
resposta esperada: 
mensagem                  id
--------                  --
Filme criado com sucesso!  id do filme

2- Listar todos os filmes (GET)
	Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/listar/" -Method GET
resposta esperada: 
aparecerá todos os filmes

3- Buscar um filme pelo ID detalhadamente (GET)
	Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/detalhar/1/" -Method GET
resposta esperada: 
id titulo    ano  genero
-- ------    ---  ------
 2 FILME , DATA , GENERO
 
4- Atualizar um filme (PUT)
	Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/atualizar/1/" -Method PUT -ContentType "application/json" -Body '{"titulo": "John Wick 2", "ano": 2017, "genero": "Action"}'
resposta esperada (por exemplo):
mensagem                      filme
--------                      -----
Filme atualizado com sucesso! @{id=2; titulo=John Wick 2; ano=2017; genero=Action}

5- curl -X DELETE 
	Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/deletar/1/" -Method DELETE
resposta esperada:
mensagem
--------
Filme deletado com sucesso!
==============================================================================================================
atenção: o TERMINAL DO POWERSHELL NAO INTERPRETA CURL DA MESMA FORMA QUE OUTROS TERMINAIS, UTILIZE COMANDOS COMO Invoke-RestMethod
por exemplo "Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/criar/" -Method Post -ContentType "application/json" -Body '{"titulo": "Inception", "ano": 2010, "genero": "Sci-Fi"}'"


do jeito que ta deu certo: Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/criar/" -Method POST -ContentType "application/json" -Body '{"titulo": "Inception", "ano": 2010, "genero": "Sci-Fi"}'
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/criar/" -Method POST -ContentType "application/json" -Body '{"titulo": "John Wick", "ano": 2014, "genero": "Action"}'


