from django.shortcuts import render
from django.views.generic.list import ListView
from django.views  import View
from django.http import HttpResponse

from . import models
from . import forms


class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.contexto = {
            "userform":forms.UseForm(data=self.request.POST or None),
            'perfilform':forms.PerfilForm(data=self.request.POST or None)


        }

        self.renderizar = render(self.request, self.template_name, self.contexto)


    def get(self, *args, **kwargs):
        return self.renderizar


# Create your views here.
class Criar(BasePerfil):
    pass


class Atualizar(BasePerfil):
    pass  


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login') 


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')  