
from django.contrib import admin
from .models import Pessoa, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'municipio',)
    search_fields = ('username', 'email',)
    ordering = ('id', 'username', 'first_name', 'last_name', 'email',)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('PESSOA', {'fields': (('id', 'nome_completo', 'user',), 'telefone', 'email',)}),)
    readonly_fields = ('id',)
    list_display = ('id', 'nome_completo', 'user', 'telefone', 'email',)
    search_fields = ('nome_completo',)
    ordering = ('id', 'nome_completo',)
    list_filter = ('municipio_de_trabalho_da_pessoa',)