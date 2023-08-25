from django.contrib import admin
from .models import (
    Item_de_orcamento,
    Orcamento_para_solicitacao_de_fundos,
    Solicitacao_de_fundos,
)

@admin.register(Item_de_orcamento)
class Item_de_orcamentoAdmin(admin.ModelAdmin):
    fields = ('id', 'nome', 'quatidade', 'unidade_de_medida', 'preco_unitario', 'preco_total_do_item',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome', 'quantidade', 'unidade_de_medida', 'preco_unitario', 'preco_total_do_item',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    list_filter = ('nome',)


@admin.register(Orcamento_para_solicitacao_de_fundos)
class Orcamento_para_solicitacao_de_fundosAdmin(admin.ModelAdmin):
    fields = ('id', 'data_do_orcamento', 'empresa_fornecedora', 'profissional_fornecedor', 'inclui', 'exclui', 'validade', 'forma_de_garantia', 'valor_total_do_orcamento', 'dados_para_pagamento',)
    readonly_fields = ('id', 'valor_total_do_orcamento',)
    list_display = ('id', 'data_do_orcamento', 'empresa_fornecedora', 'profissional_fornecedor', 'valor_total_do_orcamento',)
    search_fields = ('empresa_fornecedora', 'profissional_fornecedor',)
    ordering = ('id', 'empresa_fornecedora', 'profissional_fornecedor',)
    list_filter = ('empresa_fornecedora', 'profissional_fornecedor',)


@admin.register(Solicitacao_de_fundos)
class Solicitacao_de_fundosAdmin(admin.ModelAdmin):
    fields = ('id', 'data_da_solicitacao', 'municipio_solicitante', 'responsavel_pelo_preenchimento', 'ur_vinculada', 'projeto_vinculado', 'objetivo_especifico_vinculado', 'etapa_vinculada', 'atividade_vinculada', 'cronograma', 'urgencia', 'observacoes',)
    readonly_fields = ('id',)
    list_display = ('id', 'data_da_solicitacao', 'municipio_solicitante', 'responsavel_pelo_preenchimento', 'ur_vinculada', 'projeto_vinculado', 'objetivo_especifico_vinculado', 'etapa_vinculada', 'atividade_vinculada', 'cronograma', 'urgencia', 'observacoes',)
    search_fields = ('municipio_solicitante', 'responsavel_pelo_preenchimento',)
    ordering = ('id', 'municipio_solicitante', 'responsavel_pelo_preenchimento', 'ur_vinculada', 'projeto_vinculado', 'objetivo_especifico_vinculado', 'etapa_vinculada', 'atividade_vinculada',)
    list_filter = ('municipio_solicitante', 'responsavel_pelo_preenchimento', 'projeto_vinculado',)

