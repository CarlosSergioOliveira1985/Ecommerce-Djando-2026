from django.contrib import admin
from .models import Produto, Variacao
from . import models

# Register your models here.

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1

class ProdutoAdimin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]

admin.site.register(Produto, ProdutoAdimin)
admin.site.register(Variacao)