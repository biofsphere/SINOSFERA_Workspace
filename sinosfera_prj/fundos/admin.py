from django.contrib import admin
from django import forms
from .models import (
    Item,
    Compra,
    Orcamento,
    Requisicao,
)


class CompraInlineAdmin(admin.TabularInline):
    model = Compra
    readonly_fields = ('id', 'subtotal_da_compra',)
    fields = ('item', 'quantidade', 'unidade', 'preco_unitario', 'subtotal_da_compra',)
    extra = 1


class OrcamentoInlineAdmin(admin.TabularInline):
    model = Orcamento
    readonly_fields = ('id', 'total_do_orcamento',)
    fields = ('id', 'data', 'empresa_fornecedora', 'profissional_fornecedor', 'total_do_orcamento', 'arquivos',)
    # verbose_name_plural='Orçamentos'

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'tipo', 'unidade', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('get_item_id', 'nome', 'tipo', 'unidade', 'descricao',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('tipo', 'unidade',)


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    fields = (
        'id', 
        #'orcamento',
        'item', 
        'quantidade', 
        'unidade', 
        'preco_unitario', 
        'subtotal_da_compra',
        )
    readonly_fields = ('id', 'subtotal_da_compra',)
    list_display = ('get_item_id', 'item', 'quantidade', 'unidade', 'preco_unitario', 'subtotal_da_compra',)
    search_fields = ('item',)
    list_filter = ('item',)


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
    inlines = [CompraInlineAdmin]


@admin.register(Requisicao)
class RequisicaoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Vínculos desta solicitação', {'fields': ['projeto_vinculado', 'objetivo_especifico_vinculado', 'etapa_vinculada', 'atividade_vinculada',]}),
        ('Requisição de fundos',{ 'fields': ['id', 'fundo_solicitado', 'data', 'urgencia', 'cronograma',]}),
        ('Ancoragem', { 'fields': ['instituicao_solicitante', 'municipio', 'ur_vinculada', 'responsavel_pelo_preenchimento',]}),
        ('Observações adicionais', {'fields': ['observacoes']}),
        ('Arquivos', {'fields': ['arquivos',]}),
        ]
    readonly_fields = ('id',)
    list_display = ('id', 'fundo_solicitado', 'data', 'municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado', 'cronograma', 'urgencia', 'observacoes',)
    search_fields = ('municipio', 'responsavel_pelo_preenchimento',)
    ordering = ('id', 'municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado',)
    list_filter = ('fundo_solicitado', 'municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado',)
    inlines = [OrcamentoInlineAdmin]

