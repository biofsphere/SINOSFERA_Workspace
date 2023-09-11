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
        ('PROFISSÃO', {'fields': ['id', 'nome', 'descricao',]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'nome', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Categoria_de_plano)
class Categoria_de_planoAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('CATEGORIA DE PLANO', {'fields': ['id', 'nome', 'descricao',]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'nome', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Categoria_de_subprojeto)
class Categoria_de_subprojetoAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('CATEGORIA DE SUBPROJETO, OBJETIVO ESPECÍFICO OU META', {'fields': ['id', 'nome', 'descricao',]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'nome', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Subcategoria_de_subprojeto)
class Subcategoria_de_subprojetoAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('SUBCATEGORIA DE SUBPROJETO, OBJETIVO ESPECÍFICO OU META', {'fields': [('categoria',), 'id', 'nome', 'descricao',]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'nome', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', 'categoria',)
    search_fields = ('nome',)
    ordering = ('id', 'nome', 'categoria',)
    list_filter = ('nome', 'categoria',)


@admin.register(Categoria_de_atividade)
class Categoria_de_atividadeAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('CATEGORIA DE ATIVIDADE', {'fields': ['id', 'nome', 'descricao',]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'nome', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Subcategoria_de_atividade)
class Sub_categoria_de_atividadeAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('SUBCATEGORIA DE ATIVIDADE', {'fields': ['id', 'nome', 'descricao', 'categoria',]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'nome', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', 'categoria',)
    search_fields = ('nome',)
    ordering = ('id', 'nome', 'categoria',)
    list_filter = ('nome', 'categoria',)


@admin.register(Categoria_de_publico)
class Categoria_de_publicoAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('CATEGORIA DE PÚBLICO', {'fields': ['id', 'nome', 'descricao',]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'nome', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)


@admin.register(Categoria_de_despesa)
class Categoria_de_despesaAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('CATEGORIA DE DESPESA', {'fields': ['id', 'nome', 'descricao',]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'nome', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    search_fields = ('nome',)


@admin.register(Unidade_de_medida)
class Unidade_de_medidaAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('UNIDADE DE MEDIDA', {'fields': ['id', 'nome', 'abreviatura', 'descricao',]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'nome', 'abreviatura', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    search_fields = ('nome', 'abreviatura',)


@admin.register(Fundo)
class FundoAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('TIPO DE FUNDO', {'fields': ['id', 'nome', 'descricao',]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'nome', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', )
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)