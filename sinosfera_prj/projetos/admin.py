from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Projeto, Objetivo_especifico_de_projeto, Etapa, Atividade, Publico

class PublicoInlineAdmin(admin.TabularInline):
    model = Publico
    readonly_fields = ('id',)
    fields = ('id', 'categoria', 'quantidade', 'detalhamento',)
    extra = 1

    # def get_publico(self):
    #     publico_total = self.quantidade

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Programa vinculado',{'fields': ['programa_vinculado_ao_projeto',]}),
        ('Dados básicos do projeto',{ 'fields': ['id', 'nome', 'inicio', 'fim', 'encerrado',]}),
        ('Descrição', {'fields': ['objetivo_geral_do_projeto', 'resumo_descritivo_do_projeto',]}),
        ('Financiamento', {'fields': ['fundos_de_execucao_do_projeto', 'fundos_estimados_do_verde_sinos', 'fundos_estimados_de_contra_partida', 'valor_total_do_projeto',]}),
        ('Ancoragem', { 'fields': ['municipio_ancora_do_projeto', 'urs_vinculadas_ao_projeto', 'instituicao_ancora_do_projeto', 'pessoa_ancora_do_projeto',]}),
        ('Arquivos', {'fields': ['arquivos',]}),
        ]
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
    search_fields = ('nome',)
    ordering = ('id', 'nome', 'municipio_ancora_do_projeto', 'pessoa_ancora_do_projeto', 'valor_total_do_projeto',)
    list_filter = ('municipio_ancora_do_projeto', 'pessoa_ancora_do_projeto', 'municipio_ancora_do_projeto',)

    # Métodos de formatação dos dados na visualização da tabela
    def total_projeto_formatado(self, obj):
        return f'R${intcomma(obj.valor_total_do_projeto)}'

    def fundos_verde_sinos_formatado(self, obj):
        return f'R${intcomma(obj.fundos_estimados_do_verde_sinos)}'

    def fundos_contra_partida_formatado(self, obj):
        return f'R${intcomma(obj.fundos_estimados_de_contra_partida)}'


@admin.register(Objetivo_especifico_de_projeto)
class Objetivo_especifico_de_projetoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Projeto vinculado',{'fields': ['projeto_vinculado_ao_objetivo_especifico',]}),
        ('Objetivo específico, sub-projeto ou meta',{ 'fields': ['categoria_de_objetivo_especifico', ('id', 'nome',), ('inicio', 'fim', 'percentual_de_alcance_atingido',)]}),
        ('Descrição e método de avaliação', {'fields': ['descricao_do_objetivo_especifico', 'indicadores', 'verificacao',]}),
        # ('Financiamento', {'fields': ['',]}),
        ('Ancoragem', { 'fields': ['coordenador',]}),
        ('Arquivos', {'fields': ['arquivos',]}),
        ]
    readonly_fields = ('id',)
    list_display = ('id', 'projeto_vinculado_ao_objetivo_especifico', 'categoria_de_objetivo_especifico', 'nome', 'descricao_do_objetivo_especifico', 'coordenador', 'indicadores', 'verificacao', 'percentual_de_alcance_atingido', 'inicio', 'fim',)
    search_fields = ('nome', 'coordenador',)
    ordering = ('id', 'nome', 'coordenador',)
    list_filter = ('projeto_vinculado_ao_objetivo_especifico',)


@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Objetivo específico, sub-projeto ou meta vinculada',{'fields': ['objetivo_especifico_vinculado_a_etapa',]}),
        ('Etapa',{ 'fields': ['id', 'nome', 'concluida',]}),
        ('Descrição', {'fields': ['descricao',]}),
        # ('Financiamento', {'fields': ['',]}),
        ('Ancoragem', { 'fields': ['coordenador',]}),
        ]
    readonly_fields = ('id',)
    list_display = ('id', 'nome', 'objetivo_especifico_vinculado_a_etapa', 'descricao', 'concluida', 'coordenador',)
    search_fields = ('nome', 'coordenador',)
    ordering = ('id', 'nome', 'coordenador',)
    list_filter = ('objetivo_especifico_vinculado_a_etapa',)


@admin.register(Atividade)
class AtividadeAdmin(LeafletGeoAdmin):
    fieldsets = [
        ('Vínculos desta atividade', {'fields': [('projeto_vinculado', 'objetivo_especifico_vinculado', 'etapa_vinculada',),]}),
        ('Atividade',{ 'fields': [('id', 'categoria_de_atividade', 'sub_categoria_de_atividade',), 'nome', ('inicio', 'fim', 'concluida',),]}),
        ('Descrição', {'fields': ['descricao', 'base_curricular_vinculada',]}),
        ('Resultados', {'fields': ['publico_envolvido', 'resultados',]}),
        ('Ancoragem', { 'fields': ['municipio', 'ur_vinculada', 'coordenador',]}),
        ('Localização', {'fields': ['localizacao',]}),
        ('Arquivos', {'fields': ['arquivos',]}),
        ]
    readonly_fields = ('id', 'publico_envolvido',)
    list_display = ('get_item_id', 'nome', 'inicio', 'fim', 'concluida', 'categoria_de_atividade', 'get_publico_total', 'municipio', 'localizacao', 'projeto_vinculado',)
    search_fields = ('nome', 'coordenador',)
    ordering = ('id', 'nome', 'coordenador',)
    list_filter = ('projeto_vinculado', 'coordenador', 'municipio', 'categoria_de_atividade',)
    inlines = [PublicoInlineAdmin]

    # def total_public_attended(self, obj):
    #     # Display the total public attended for the current activity
    #     return obj.total_public_attended()
    # total_public_attended.short_description = 'Total Public Attended'
