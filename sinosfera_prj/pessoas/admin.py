
from django.contrib import admin
from .models import Pessoa, CustomUser
from core.mixins import CreateUpdateUserAdminMixin

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('get_item_id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active',)
    search_fields = ('username', 'email',)
    ordering = ('id', 'username', 'first_name', 'last_name', 'email',)


@admin.register(Pessoa)
class PessoaAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('PESSOA', {'fields': ['id', 'conta_associada', ('nome_completo',), ('telefone_celular', 'email',), ('profissao', 'municipio_de_trabalho_da_pessoa',),]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'id_codificada', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'conta_associada', 'id_codificada', 'nome_completo', 'telefone_celular', 'email', 'municipio_de_trabalho_da_pessoa', 'criado_por', 'criado_em',)
    search_fields = ('nome_completo', 'municipio_de_trabalho_da_pessoa',)
    ordering = ('id', 'nome_completo','municipio_de_trabalho_da_pessoa',)
    list_filter = ('municipio_de_trabalho_da_pessoa',)