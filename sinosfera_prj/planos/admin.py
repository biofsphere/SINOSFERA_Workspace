from django.contrib import admin
from .models import Plano, Programa_de_acoes_prioritarias, Acao_prioritaria

@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    fields = ('id', 'categoria', 'nome', 'objetivo_geral_do_plano', 'resumo_descritivo_do_plano', 'fundos_de_execucao_do_plano', 'prazo_de_execucao_do_plano', 'escopo_geografico_do_plano', 'municipio_ancora_do_plano', 'instituicao_ancora_do_plano', 'pessoa_ancora_do_plano',)
    readonly_fields = ('id',)
    list_display = ('id', 'categoria', 'nome', 'prazo_de_execucao_do_plano', 'escopo_geografico_do_plano', 'municipio_ancora_do_plano', 'instituicao_ancora_do_plano', 'pessoa_ancora_do_plano',)
    # search_fields = ('nome_completo',)
    # ordering = ('id', 'nome_completo',)
    # list_filter = ('municipio_ancora_do_plano',)


@admin.register(Programa_de_acoes_prioritarias)
class Programa_de_acoes_prioritariasAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'plano_vinculado_ao_programa_de_acoes_prioritarias', 'objetivo_geral_do_programa_de_acoes_prioritarias', 'coordenador',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome', 'plano_vinculado_ao_programa_de_acoes_prioritarias', 'coordenador',)
    # search_fields = ('nome_completo',)
    # ordering = ('id', 'nome_completo',)
    # list_filter = ('municipio_de_trabalho_da_pessoa',)


@admin.register(Acao_prioritaria)
class Acao_prioritariaAdmin(admin.ModelAdmin):
    fields = ('id', 'programa_de_acoes_prioritarias_vinculado', 'nome', 'objetivo_geral', 'coordenador', )
    readonly_fields = ('id',)
    list_display = ('id',  'programa_de_acoes_prioritarias_vinculado', 'nome', 'coordenador',)
    # search_fields = ('nome',)
    # ordering = ('id', 'nome',)
    # list_filter = ('municipio_de_trabalho_da_pessoa',)