from django.contrib import admin
from .models import (
    Profissao, 
    Categoria_de_plano, 
    Sub_categoria_de_objetivo_especifico, 
    Categoria_de_objetivo_especifico, 
    Sub_categoria_de_atividade, 
    Categoria_de_atividade,
)

@admin.register(Profissao)
class ProfissaoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Categoria_de_plano)
class Categoria_de_planoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Categoria_de_objetivo_especifico)
class Categoria_de_objetivo_especificoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Sub_categoria_de_objetivo_especifico)
class Sub_categoria_de_objetivo_especificoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Categoria_de_atividade)
class Categoria_de_atividadeAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Sub_categoria_de_atividade)
class Sub_categoria_de_atividadeAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)