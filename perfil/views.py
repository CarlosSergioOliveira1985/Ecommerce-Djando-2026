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

        self.perfil = None
        
        if self.request.user.is_authenticated:
            self.perfil = models.Perfil.objects.filter(useruario=self.request.user).first()
            self.contexto = {
                "userform": forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user, 
                    instance=self.request.user,
                ),
                "perfilform": forms.PerfilForm(
                    data=self.request.POST or None,
                    instance=self.perfil
                ),
            }
            
        else:
            self.contexto = {
                "userform": forms.UserForm(data=self.request.POST or None),
                "perfilform": forms.PerfilForm(data=self.request.POST or None),
            }

        # Sempre define renderizar
        self.renderizar = render(self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar



# Create your views here.
class Criar(BasePerfil):
    def post(self, *args, **kwargs ):
        if not self.contexto['userform'].is_valid() or not self.contexto['perfilform'].is_valid():
            print("Inválido")
            return self.renderizar 
        print("Valido")
        return self.renderizar    


class Atualizar(BasePerfil):
    pass  


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login') 


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')  