from django.db import models
from veiculo.consts import OPCOES_MARCAS, OPCOES_COMBUSTIVEIS, OPCOES_CORES

class Veiculo(models.Model):
    marca = models.PositiveSmallIntegerField(choices= OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    combustivel = models.PositiveSmallIntegerField(choices= OPCOES_COMBUSTIVEIS)
    cor = models.PositiveSmallIntegerField (choices= OPCOES_CORES )
    
    
   