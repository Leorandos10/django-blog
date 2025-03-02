from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano = models.CharField(max_length=4, blank=True, null=True)
    genero = models.CharField(max_length=100, blank=True, null=True)
    diretor = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
