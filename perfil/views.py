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
            self.perfil = models.Perfil.objects.filter(self.request.user).first()
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
            return self.renderizar 

        username = self.contexto['userform'].cleaned_data.get('username')
        password = self.contexto['userform'].cleaned_data.get('password')
        email = self.contexto['userform'].cleaned_data.get('email')

        # ususário logado 
        if self.request.user.is_authenticated:
            pass

        # usuário não logado (novo)
        else:
            usuario = self.contexto['userform'].save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = self.contexto['perfilform'].save(commit=False)
            perfil.useruario = usuario
            perfil.save()

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