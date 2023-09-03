from django.contrib import admin
from .models import (
    Profissao, 
    Categoria_de_plano, 
    Sub_categoria_de_objetivo_especifico, 
    Categoria_de_objetivo_especifico, 
    Sub_categoria_de_atividade, 
    Categoria_de_atividade,
    Categoria_de_publico,
    Unidade_de_medida,
    Fundo,
)


@admin.register(Profissao)
class ProfissaoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('get_item_id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Categoria_de_plano)
class Categoria_de_planoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('get_item_id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Categoria_de_objetivo_especifico)
class Categoria_de_objetivo_especificoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('get_item_id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Sub_categoria_de_objetivo_especifico)
class Sub_categoria_de_objetivo_especificoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('get_item_id', 'nome',)
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


@admin.register(Sub_categoria_de_atividade)
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