from django.contrib import admin
from django import forms
from .models import (
    Item,
    Pedido,
    Orcamento,
    Solicitacao_de_fundos,
)


class PedidoInlineAdmin(admin.TabularInline):
    model = Pedido
    extra = 1


class OrcamentoInlineAdmin(admin.TabularInline):
    model = Orcamento

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'tipo', 'unidade', 'descricao',)
    readonly_fields = ('id',)
    list_display = ('get_item_id', 'nome', 'tipo', 'unidade', 'descricao',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('tipo', 'unidade',)


@admin.register(Pedido)
class Pedido_de_itemAdmin(admin.ModelAdmin):
    fields = ('id', 'orcamento', 'item', 'quantidade', 'unidade', 'preco_unitario', 'total_do_pedido_do_item',)
    readonly_fields = ('id', 'total_do_pedido_do_item',)
    list_display = ('get_item_id', 'item', 'quantidade', 'unidade', 'preco_unitario', 'total_do_pedido_do_item',)
    search_fields = ('item',)
    list_filter = ('item',)


@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    fields = ('id', 'data', 'empresa_fornecedora', 'profissional_fornecedor', 'exclui', 'validade', 'forma_de_garantia', 'total_do_orcamento', 'dados_para_pagamento', 'observacoes',)
    readonly_fields = ('id', 'total_do_orcamento',)
    list_display = ('get_item_id', 'data', 'empresa_fornecedora', 'profissional_fornecedor', 'total_do_orcamento',)
    search_fields = ('empresa_fornecedora', 'profissional_fornecedor',)
    ordering = ('id', 'empresa_fornecedora', 'profissional_fornecedor',)
    list_filter = ('empresa_fornecedora', 'profissional_fornecedor',)
    inlines = [PedidoInlineAdmin]


@admin.register(Solicitacao_de_fundos)
class Solicitacao_de_fundosAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Vínculos desta solicitação', {'fields': ['projeto_vinculado', 'objetivo_especifico_vinculado', 'etapa_vinculada', 'atividade_vinculada',]}),
        ('Solicitação de fundos',{ 'fields': ['id', 'fundo_solicitado', 'data', 'urgencia', 'cronograma',]}),
        ('Ancoragem', { 'fields': ['instituicao_solicitante', 'municipio', 'ur_vinculada', 'responsavel_pelo_preenchimento',]}),
        ('Orçamentos', {'fields': ['observacoes']}),
        ('Arquivos', {'fields': ['arquivos',]}),
        ]
    readonly_fields = ('id',)
    list_display = ('id', 'fundo_solicitado', 'data', 'municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado', 'cronograma', 'urgencia', 'observacoes',)
    search_fields = ('municipio', 'responsavel_pelo_preenchimento',)
    ordering = ('id', 'municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado',)
    list_filter = ('fundo_solicitado', 'municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado',)
    inlines = [OrcamentoInlineAdmin]

