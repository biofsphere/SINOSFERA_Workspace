
from django.contrib import admin
from .models import Pessoa, CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active',)
    search_fields = ('username', 'email',)
    ordering = ('id', 'username', 'first_name', 'last_name', 'email',)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('PESSOA', {'fields': (('id', 'nome_completo', 'usuario',), 'telefone_celular', 'email',)}),)
    readonly_fields = ('id',)
    list_display = ('id', 'nome_completo', 'usuario', 'telefone_celular', 'email',)
    search_fields = ('nome_completo',)
    ordering = ('id', 'nome_completo',)
    list_filter = ('municipio_de_trabalho_da_pessoa',)