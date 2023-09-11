from django.contrib import admin
from core.mixins import CreateUpdateUserAdminMixin
from .models import (
    Profissao, 
    Categoria_de_plano, 
    Subcategoria_de_subprojeto, 
    Categoria_de_subprojeto, 
    Subcategoria_de_atividade, 
    Categoria_de_atividade,
    Categoria_de_publico,
    Categoria_de_despesa,
    Unidade_de_medida,
    Fundo,
)


@admin.register(Profissao)
class ProfissaoAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('PROFISSÃO', {'fields': ['id_codificada', 'nome', 'descricao',]}),
        ('SISTEMA', {'fields': ['id', ('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'id_codificada', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id_codificada', 'nome', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    search_fields = ('nome',)
    ordering = ('id_codificada', 'nome',)
    list_filter = ('nome',)


@admin.register(Categoria_de_plano)
class Categoria_de_planoAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao', 'criado_por', 'criado_em',)
    readonly_fields = ('id', 'criado_por', 'criado_em',)
    list_display = ('get_item_id', 'nome', 'criado_por', 'criado_em',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Categoria_de_subprojeto)
class Categoria_de_subprojetoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao', 'criado_por', 'criado_em',)
    readonly_fields = ('id', 'criado_por', 'criado_em',)
    list_display = ('get_item_id', 'nome', 'criado_por', 'criado_em',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Subcategoria_de_subprojeto)
class Sub_categoria_de_objetivo_especificoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao', 'criado_por', 'criado_em',)
    readonly_fields = ('id',)
    list_display = ('get_item_id', 'nome', 'criado_por', 'criado_em',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Categoria_de_atividade)
class Categoria_de_atividadeAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('get_item_id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Subcategoria_de_atividade)
class Sub_categoria_de_atividadeAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('get_item_id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Categoria_de_publico)
class Categoria_de_publicoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    # list_filter = ('nome',)


@admin.register(Categoria_de_despesa)
class Categoria_de_despesaAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    search_fields = ('nome',)


@admin.register(Unidade_de_medida)
class Unidade_de_medidaAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'abreviatura', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome', 'abreviatura',)
    search_fields = ('nome', 'abreviatura',)


@admin.register(Fundo)
class FundoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)