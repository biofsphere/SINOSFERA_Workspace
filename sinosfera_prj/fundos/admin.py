from django.contrib import admin
from django import forms
from .models import (
    Item,
    Orcamento,
    Requisicao,
)


class ItemInlineAdmin(admin.TabularInline):
    model = Item
    readonly_fields = ('id', 'subtotal_do_item',)
    fields = ('id', 'tipo', 'nome', 'descricao', 'unidade', 'quantidade', 'preco_unitario', 'subtotal_do_item',)
    extra = 1


class OrcamentoInlineAdmin(admin.TabularInline):
    model = Orcamento
    readonly_fields = ('id', 'total_do_orcamento',)
    fields = ('id', 'data', 'empresa_fornecedora', 'profissional_fornecedor', 'total_do_orcamento', 'arquivos',)



@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('id', 'tipo', 'nome', 'descricao', 'unidade', 'quantidade', 'preco_unitario', 'subtotal_do_item',)
    readonly_fields = ('id', 'subtotal_do_item',)
    list_display = ('get_item_id', 'tipo', 'nome', 'descricao', 'unidade', 'quantidade', 'preco_unitario', 'subtotal_do_item',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('tipo', 'unidade',)


@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    fields = (
        'requisicao',
        'id', 
        'data', 
        'empresa_fornecedora',
        'numero_NF',
        'data_NF', 
        'profissional_fornecedor',
        'numero_RPA',
        'data_RPA', 
        'validade', 
        'forma_de_garantia', 
        'total_do_orcamento', 
        'dados_para_pagamento', 
        'exclui', 
        'observacoes', 
        'arquivos',)
    readonly_fields = ('id', 'total_do_orcamento',)
    list_display = ('get_item_id', 'data', 'empresa_fornecedora', 'profissional_fornecedor', 'total_do_orcamento',)
    search_fields = ('empresa_fornecedora', 'profissional_fornecedor',)
    ordering = ('id', 'empresa_fornecedora', 'profissional_fornecedor',)
    list_filter = ('empresa_fornecedora', 'profissional_fornecedor',)
    inlines = [ItemInlineAdmin]


@admin.register(Requisicao)
class RequisicaoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Vínculos desta requisição', {'fields': ['projeto_vinculado', 'objetivo_especifico_vinculado', 'etapa_vinculada', 'atividade_vinculada',]}),
        ('Requisição de fundos',{ 'fields': ['id', 'fundo_solicitado', 'data', 'urgencia', 'cronograma',]}),
        ('Ancoragem', { 'fields': ['instituicao_solicitante', 'municipio', 'ur_vinculada', 'responsavel_pelo_preenchimento', 'criado_por', 'atualizado_por',]}),
        ('Observações adicionais', {'fields': ['observacoes']}),
        ('Arquivos', {'fields': ['arquivos',]}),
        ]
    readonly_fields = ('id', 'criado_por', 'atualizado_por',)
    list_display = ('get_item_id', 'fundo_solicitado', 'data', 'municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado', 'urgencia', 'criado_por', 'atualizado_por',)
    search_fields = ('municipio', 'responsavel_pelo_preenchimento',)
    ordering = ('id', 'municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado',)
    list_filter = ('fundo_solicitado', 'municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado',)
    inlines = [OrcamentoInlineAdmin]

