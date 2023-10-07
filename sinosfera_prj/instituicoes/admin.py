from django.contrib import admin
from .models import Instituicao
# from core.admin import custom_admin_site

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    fields = ('id', 'razao_social', 'nome_fantasia', 'sem_cnpj', 'cnpj', 'telefone', 'email', 'url', 'responsavel_pela_instituicao',)
    readonly_fields = ('id',)
    list_display = ('id', 'razao_social', 'nome_fantasia', 'sem_cnpj', 'cnpj', 'telefone', 'email', 'url', 'responsavel_pela_instituicao',)
    search_fields = ('nome_fantasia', 'cnpj', 'responsavel_pela_instituicao',)
    ordering = ('id', 'nome_fantasia', 'responsavel_pela_instituicao',)
    # list_filter = ('municipio',)
