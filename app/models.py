from django.db import models


class Usuario(models.Model):
    cod = models.IntegerField()
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.cod) + ' - ' + self.nome
