from django.db import models


class Usuario(models.Model):
    cod = models.IntegerField()
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.cod) + ' - ' + self.nome


class Municipios(models.Model):
    geom = models.TextField(blank=True, null=True)
    codigo = models.CharField(max_length=7, blank=True, null=True)
    nome = models.CharField(max_length=60, blank=True, null=True)
    sigla_uf = models.CharField(max_length=2, blank=True, null=True)
    area_km2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipios'

class Estados(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    codigo = models.CharField(max_length=2, blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    sigla_uf = models.CharField(max_length=2, blank=True, null=True)
    nm_regiao = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'