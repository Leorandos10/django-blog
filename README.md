# Meu Projeto Django

Este é um projeto Django simples que implementa um sistema CRUD com autenticação por tokens e consumo de API externa.

## Requisitos

- Python 3.10+
- Django
- Django REST Framework
- Docker & Docker Compose
- Git
- MySQL ou PostgreSQL

## Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados e aplique as migrações:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## Uso com Docker

Para rodar o projeto com Docker:
```bash
docker-compose up --build
```

## Endpoints da API

- `GET /api/` - Lista os recursos
- `POST /api/` - Cria um novo recurso
- `GET /api/{id}/` - Detalhes de um recurso
- `PUT /api/{id}/` - Atualiza um recurso
- `DELETE /api/{id}/` - Exclui um recurso

## Contribuição

1. Crie um branch:
   ```bash
   git checkout -b minha-feature
   ```
2. Faça suas alterações e commite:
   ```bash
   git commit -m "feat: minha nova feature"
   ```
3. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
4. Abra um Pull Request!


