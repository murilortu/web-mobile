from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect 


class Login(View):
        
    def get(self, request):
        contexto = {}
        return render(request, 'autenticacao.html', contexto)
    

    def post(self, request):
        
        usuario = request.POST.get('usuario' or None)
        senha = request.POST.get('senha' or None)

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:

            if user.is_active:
                login(request, user)
                return render(request, 'listar_veiculos.html', {})
            
            return render(request, 'autenticacao.html', {'messagem': 'Usuário inativo!'})

        print(usuario, senha)
        return render(request, 'autenticacao.html', {'messagem': 'Usuário ou senha inválidos!'})
    
class Cadastro(View):
    def get(self, request):
        contexto = {}
        return render(request, 'cadastro.html', contexto)