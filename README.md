# Meu Projeto Django

Este é um projeto Django simples que implementa um sistema CRUD com autenticação por tokens e consumo de API externa.

## Requisitos
- Python 3.10+
- Django
- Django REST Framework
- Docker & Docker Compose
- Git
- MySQL ou PostgreSQL
=============================================================================================================-
O projeto apresenta: 
- CRUD Completo
- Consumo de API Externa: API OMDb
- Arquivos necessários e diferenciais como: .gitignore, requirements.txt, README.md, Dockerfile e docker-compose.yml
- 
==============================================================================================================
Para a criação manual pelo terminal utilize:

1- criar um filme POST
utilize o comando: Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/criar/" -Method POST -ContentType "application/json" -Body '{"titulo": "nome", "ano": 2014, "genero": "Action"}'
resposta esperada: 
Filme criado com sucesso!  id do filme

2- Listar todos os filmes (GET)
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/listar/" -Method GET
resposta esperada: 
aparecerá todos os filmes

3- Buscar um filme pelo ID detalhadamente (GET)
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/detalhar/id/" -Method GET
resposta esperada: 
id titulo    ano  genero
2 FILME , DATA , GENERO
 
4- Atualizar um filme (PUT)
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/atualizar/1/" -Method PUT -ContentType "application/json" -Body '{"titulo": "John Wick 2", "ano": 2017, "genero": "Action"}'
resposta esperada (por exemplo):
Filme atualizado com sucesso! @{id=2; titulo=John Wick 2; ano=2017; genero=Action}

5- curl -X DELETE 
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/deletar/1/" -Method DELETE
resposta esperada:
Filme deletado com sucesso!

==============================================================================================================
atenção: o TERMINAL DO POWERSHELL NAO INTERPRETA CURL DA MESMA FORMA QUE OUTROS TERMINAIS, UTILIZE COMANDOS COMO "Invoke-RestMethod"
por exemplo "Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/criar/" -Method Post -ContentType "application/json" -Body '{"titulo": "Inception", "ano": 2010, "genero": "Sci-Fi"}'"


do jeito que ta deu certo: Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/criar/" -Method POST -ContentType "application/json" -Body '{"titulo": "Inception", "ano": 2010, "genero": "Sci-Fi"}'
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/filme/criar/" -Method POST -ContentType "application/json" -Body '{"titulo": "John Wick", "ano": 2014, "genero": "Action"}'

=============================================================================================================

-crie seus filmes no index.html, acessando pelo IP padrão http://127.0.0.1:8000 

-pesquise algum filme http://127.0.0.1:8000/api/filme/listar/?titulo=NOMEdoFILME

alguns filmes de exemplo: Fight Club, Inception, Interstellar, Blade Runner 2049, Shrek