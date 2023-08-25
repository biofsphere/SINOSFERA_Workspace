
from django.contrib import admin
from .models import Pessoa, CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active',)
    search_fields = ('username', 'email',)
    ordering = ('id', 'username', 'first_name', 'last_name', 'email',)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('PESSOA', {'fields': (('id', 'nome_completo', 'usuario',), 'telefone_celular', 'email', 'profissao', 'municipio_de_trabalho_da_pessoa',)}),)
    readonly_fields = ('id',)
    list_display = ('id', 'nome_completo', 'usuario', 'telefone_celular', 'email', 'municipio_de_trabalho_da_pessoa',)
    search_fields = ('nome_completo', 'municipio_de_trabalho_da_pessoa',)
    ordering = ('id', 'nome_completo','municipio_de_trabalho_da_pessoa',)
    list_filter = ('municipio_de_trabalho_da_pessoa',)