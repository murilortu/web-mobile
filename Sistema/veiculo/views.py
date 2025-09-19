from django.shortcuts import render
from veiculo.models import Veiculo
from django.views.generic import ListView



class ListarVeiculos(ListView):
    model = Veiculo
    template_name = 'veiculo/listar_veiculos.html'
    context_object_name = 'veiculos/listar_veiculos'  # Nome do contexto para usar no template



