from django.contrib import admin
from django import forms
from core.mixins import CreateUpdateUserAdminMixin
from .models import (
    Item,
    Pedido,
    Orcamento,
    Requisicao,
)


class PedidoInlineAdmin(CreateUpdateUserAdminMixin, admin.TabularInline):
    model = Pedido
    readonly_fields = ('id_codificada', 'subtotal_do_item', 'criado_por', 'atualizado_por',)
    fields = ('id_codificada', 'item', 'especificacao', 'quantidade', 'preco_unitario', 'subtotal_do_item',)
    extra = 1


class OrcamentoInlineAdmin(admin.TabularInline):
    model = Orcamento
    readonly_fields = ('id', 'id_codificada', 'total_do_orcamento',)
    fields = ('id', 'id_codificada', 'data', 'empresa_fornecedora', 'profissional_fornecedor', 'total_do_orcamento', 'arquivos',)


@admin.register(Item)
class ItemAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fields = ('id', 'id_codificada', 'nome', 'unidade', 'descricao', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    readonly_fields = ('id', 'id_codificada', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id_codificada', 'nome', 'unidade', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    # list_filter = ('nome',)


@admin.register(Pedido)
class PedidoAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('ORÇAMENTO VINCULADO', {'fields': ['orcamento',]}),
        ('TIPO DE DESPESA', {'fields': ['tipo']}),
        ('ITEM', {'fields': [('id', 'id_codificada'), ('item', 'especificacao',), ('quantidade', 'preco_unitario',),]}),
        ('SUBTOTAL DO ITEM', {'fields': ['subtotal_do_item',]}),
        ('SISTEMA', {'fields': [('criado_por', 'criado_em',), ('atualizado_por', 'atualizado_em',),]}),
        )
    readonly_fields = ('id', 'id_codificada', 'subtotal_do_item', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em',)
    list_display = ('id', 'id_codificada', 'tipo', 'item', 'especificacao', 'quantidade', 'preco_unitario', 'subtotal_do_item',)
    search_fields = ('item',)
    ordering = ('id', 'item',)
    list_filter = ('tipo',)
    


@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    fields = (
        'requisicao',
        'id',
        'id_codificada', 
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
    readonly_fields = ('id', 'id_codificada', 'total_do_orcamento',)
    list_display = ('id', 'id_codificada', 'data', 'empresa_fornecedora', 'profissional_fornecedor', 'total_do_orcamento',)
    search_fields = ('empresa_fornecedora', 'profissional_fornecedor',)
    ordering = ('id', 'empresa_fornecedora', 'profissional_fornecedor',)
    list_filter = ('empresa_fornecedora', 'profissional_fornecedor',)
    inlines = [PedidoInlineAdmin]


@admin.register(Requisicao)
class RequisicaoAdmin(CreateUpdateUserAdminMixin, admin.ModelAdmin):
    fieldsets = [
        ('Vínculos desta requisição', {'fields': ['projeto_vinculado', 'subprojeto_vinculado', 'etapa_vinculada', 'atividade_vinculada',]}),
        ('Requisição de fundos',{ 'fields': ['id', 'id_codificada', 'fundo_solicitado', 'data', 'urgencia', 'cronograma',]}),
        ('Ancoragem', { 'fields': ['instituicao_solicitante', 'municipio', 'ur_vinculada', 'responsavel_pelo_preenchimento', 'criado_por', 'atualizado_por',]}),
        ('Observações adicionais', {'fields': ['observacoes']}),
        ('Arquivos', {'fields': ['arquivos',]}),
        ]
    date_hierarchy = 'data'
    readonly_fields = ('id', 'id_codificada', 'criado_por', 'atualizado_por',)
    list_display = ('id', 'id_codificada', 'fundo_solicitado', 'data', 'municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado', 'urgencia', 'criado_por', 'atualizado_por',)
    search_fields = ('municipio', 'responsavel_pelo_preenchimento',)
    ordering = ('id', 'municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado',)
    list_filter = ('municipio', 'responsavel_pelo_preenchimento', 'projeto_vinculado',)
    inlines = [OrcamentoInlineAdmin]

