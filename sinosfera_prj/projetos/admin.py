from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Projeto, Objetivo_especifico_de_projeto, Etapa, Atividade

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    fields = (
        'id', 
        'programa_vinculado_ao_projeto', 
        'nome', 'objetivo_geral_do_projeto', 
        'encerrado', 'resumo_descritivo_do_projeto', 
        'fundos_de_execucao_do_projeto', 
        'fundos_estimados_do_verde_sinos', 
        'fundos_estimados_de_contra_partida', 
        'valor_total_do_projeto', 
        'municipio_ancora_do_projeto', 
        'urs_vinculadas_ao_projeto', 
        'instituicao_ancora_do_projeto', 
        'pessoa_ancora_do_projeto', 
        'inicio', 
        'fim',
        )
    readonly_fields = ('id', 'valor_total_do_projeto',)
    list_display = (
        'id',
        'programa_vinculado_ao_projeto', 
        'nome', 
        'encerrado', 
        'fundos_verde_sinos_formatado', # method call to express in currency
        'fundos_contra_partida_formatado', # method call to express in currency 
        'total_projeto_formatado', # method call to express in currency
        'municipio_ancora_do_projeto', 
        'instituicao_ancora_do_projeto', 
        'pessoa_ancora_do_projeto', 
        'inicio', 
        'fim',
        )
    search_fields = ('nome', 'pessoa_ancora_do_projeto',)
    ordering = ('id', 'nome', 'municipio_ancora_do_projeto', 'pessoa_ancora_do_projeto', 'valor_total_do_projeto',)
    list_filter = ('municipio_ancora_do_projeto',)

    def total_projeto_formatado(self, obj):
        return f'R${intcomma(obj.valor_total_do_projeto)}'

    def fundos_verde_sinos_formatado(self, obj):
        return f'R${intcomma(obj.fundos_estimados_do_verde_sinos)}'

    def fundos_contra_partida_formatado(self, obj):
        return f'R${intcomma(obj.fundos_estimados_de_contra_partida)}'

@admin.register(Objetivo_especifico_de_projeto)
class Objetivo_especifico_de_projetoAdmin(admin.ModelAdmin):
    fields = ('id', 'projeto_vinculado_ao_objetivo_especifico', 'categoria_de_objetivo_especifico', 'nome', 'descricao_do_objetivo_especifico', 'coordenador', 'indicadores', 'verificacao', 'percentual_de_alcance_atingido', 'inicio', 'fim',)
    readonly_fields = ('id',)
    list_display = ('id', 'projeto_vinculado_ao_objetivo_especifico', 'categoria_de_objetivo_especifico', 'nome', 'descricao_do_objetivo_especifico', 'coordenador', 'indicadores', 'verificacao', 'percentual_de_alcance_atingido', 'inicio', 'fim',)
    search_fields = ('nome', 'coordenador',)
    ordering = ('id', 'nome', 'coordenador',)
    list_filter = ('projeto_vinculado_ao_objetivo_especifico',)


@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'objetivo_especifico_vinculado_a_etapa', 'descricao', 'concluida', 'coordenador',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome', 'objetivo_especifico_vinculado_a_etapa', 'descricao', 'concluida', 'coordenador',)
    search_fields = ('nome', 'coordenador',)
    ordering = ('id', 'nome', 'coordenador',)
    list_filter = ('objetivo_especifico_vinculado_a_etapa',)


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    fields = ('id', 'projeto_vinculado', 'objetivo_especifico_vinculado', 'etapa_vinculada', 'nome', 'descricao', 'inicio', 'fim', 'concluida', 'base_curricular_vinculada', 'categoria_de_atividade', 'municipio', 'ur_vinculada',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome', 'projeto_vinculado', 'nome', 'inicio', 'fim', 'concluida', 'categoria_de_atividade', 'municipio',)
    search_fields = ('nome', 'coordenador',)
    ordering = ('id', 'nome', 'coordenador',)
    list_filter = ('projeto_vinculado', 'coordenador', 'municipio', 'categoria_de_atividade',)
