from django.contrib import admin
from .models import Programa, Diretriz_especifica_de_programa

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'objetivo_geral_do_programa', 'resumo_descritivo_do_programa', 'plano_vinculado_ao_programa', 'fundos_de_execucao_do_programa', 'prazo_de_execucao_do_programa', 'escopo_geografico_do_programa', 'municipio_ancora_do_programa', 'instituicao_ancora_do_programa', 'pessoa_ancora_do_programa',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome', 'plano_vinculado_ao_programa', 'prazo_de_execucao_do_programa', 'escopo_geografico_do_programa', 'municipio_ancora_do_programa', 'instituicao_ancora_do_programa', 'pessoa_ancora_do_programa',)
    # search_fields = ('nome',)
    # ordering = ('id', 'nome',)
    # list_filter = ('municipio_ancora_do_programa',)


@admin.register(Diretriz_especifica_de_programa)
class Diretriz_especifica_de_programaAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao_da_diretriz_especifica', 'programa_vinculado_a_diretriz_especifica',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    # search_fields = ('nome',)
    # ordering = ('id', 'nome',)
    # list_filter = ('municipio_ancora_do_programa',)