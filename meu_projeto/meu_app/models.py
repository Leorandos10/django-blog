from django.db import models


class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano = models.CharField(max_length=4)
    diretor = models.CharField(max_length=255, blank=True, null=True)
    genero = models.CharField(max_length=255, blank=True, null=True)
    imdb_id = models.CharField(max_length=20, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
