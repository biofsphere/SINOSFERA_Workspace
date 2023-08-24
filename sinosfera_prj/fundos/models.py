from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User

#======================================#
#== TABELA DE SOLICITAÇÕES DE FUNDOS ==#
#======================================#


class Item_de_orcamento(models.Model):
    """Tabela de inserção de dados de item de orçamento, seja este item serviço, material ou maquinário."""
    orcamento = models.ForeignKey(
        'orcamento_para_solicitacao_de_fundos',
        on_delete=models.CASCADE,
        related_name='itens_orcados',
    )
    nome = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        help_text='Insira o nome to serviço, material ou maquinário (item de orçamento)',
    )
    quantidade = models.PositiveIntegerField(
        help_text='Especifique a quantidade que deseja adquirir considerando a unidade de medida especificada.',
    )
    unidade_de_medida = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text='Especifique a unidade de medida deste ítem de orçamento',
    )    
    preco_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Especifique o preço unitário do item de orçamento.',
    )
    preco_total_do_item = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
    )

    def save(self, *args, **kwargs):
        self.preco_total_do_item = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return 'ITE' + str(self.id).zfill(6) + '-' + self.nome
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Item de orçamento'
        verbose_name_plural = 'Itens de orçamento'   


class orcamento_para_solicitacao_de_fundos(models.Model):
    """Tabela de inserção de dados dos orçamentos para solicitação de fundos."""
    TIPOS_DE_ORCAMENTOS = [
        ('MO', 'Mão de obra e/ou serviços'),
        ('MT', 'Materiais e/ou insumos'),
        ('MQ', 'Máquinas e/ou equipamentos'),
        ]
    data_do_orcamento = models.DateField(
        help_text='Identifique o orçamento informado a sua data de emissão e selecione a data aqui.',
        blank=True,
        null=True,
    )
    empresa_fornecedora = models.ForeignKey(
        'instituicoes.Instituicao',
        on_delete=models.SET_NULL,
        help_text='Seleciona a instituição fornecedora do orçamento. Se não houver, clique em "+" para inserir.',
        blank=True,
        null=True,
        verbose_name='Empresa fornecedora',
        )
    profissional_fornecedor = models.ForeignKey(
        'pessoas.Pessoa',
        on_delete=models.SET_NULL,
        help_text='Selecione o profissional fornecedor. Senão houver, clieque em "+" para inserir.',
        blank=True,
        null=True,
        )
    inclui = models.TextField(
        'Descritivo do que está incluso no orçamento',
        help_text='Descreva tudo que está icluso no valor total do orçamento, especificando detalhes dos serviços quando for o caso.',
        blank=True,
        null=True,
    )
    exclui = models.TextField(
        'Descritivo do que não está incluso no orçamento',
        help_text='Descreva o que o orçameto não inclui, quando pertinente.',
        blank=True,
        null=True,
    )
    validade = models.PositiveIntegerField(
        help_text='Especifique em número de dias a validade do orçamento.',
        blank=True,
        null=True,
    )
    forma_de_garantia = models.CharField(
        max_length=200,
        help_text='Explicite a forma e tempo de garantia do produto ou serviços estabelecida pelo fornecedor.',
        blank=True,
        null=True,
    )
    valor_total_do_orcamento = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        )
    dados_para_pagamento = models.TextField(
        'Dados para pagamento',
        help_text='Inclua os dados para pagamento deste orçamento conforme preferência do fornecedor.'
        blank=True,
        null=True,
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to='fundos/orcamentos', 
        blank=True, 
        null=True,
        )
    
    def save_model(self, request, obj, form, change):
        """Grava usuário logado que gravou o item"""
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.atualiza_valor_total_do_orcamento()

    def atualiza_valor_total_do_orcamento(self):
        self.valor_total_do_orcamento = sum(item.preco_total_do_item for item in self.itens_orcados.all())

    def __str__(self):
        return 'ORC' + str(self.id).zfill(5)


    class Meta:
        ordering = ('id',)
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'   



class Solicitacao_de_fundos(models.Model):
    """Tabela de inserção de dados para solicitação de fundos."""
    municipio_solicitante = models.ForeignKey(
        'locais.Municipio',
        on_delete=models.NULL,
        help_text='Selecione o município para onde irão os fundos',
        blank=True,
        null=True,
        verbose_name='Município vinculado à solicitação de fundos',
        )
    responsavel_pelo_preenchimento = models.ForeignKey(
        'pessoas.Pessoa',
        on_delete=models.NULL,
        help_text='Selecione a pessoa responsável pelo preenchimento desta solicitação.',
        blank=True,
        null=True,
        verbose_name='Responsável pelo preenchimento da solicitação de fundos',
        )
    # == VÍNCULOS DA ATIVIDADE == #
    ur_vinculada = models.OneToOneField(
        'locais.Unidade_de_referencia',
        on_delete=models.NULL,
        help_text='Selecione a UR a que esta solicitação está diretamente vinculada, se houver.',
        blank=True,
        null=True,
        verbose_name='UR vinculada à solicitação de fundos',
        )    
    projeto_vinculado = models.ForeignKey(
        'projetos.Projeto', 
        on_delete=models.NULL, 
        help_text='Selecione o projeto a que esta solicitação está diretamente vinculada.',
        blank=True, 
        null=True, 
        verbose_name='Projeto vinculado à solicitação de fundos', 
        )
    objetivo_especifico_vinculado = models.ForeignKey(
        'projetos.Objetivo_especifico_de_projeto', 
        on_delete=models.SET_NULL, 
        help_text='Selecione o objetivo específico a que esta solicitação está diretamente vincula.', 
        blank=True, 
        null=True, 
        verbose_name='Objetivo específico vinculado à solicitação de fundos', 
        )
    etapa_vinculada = models.ForeignKey(
        'projetos.Etapa', 
        on_delete=models.SET_NULL, 
        help_text='Selecione a(s) etapa(s) a que esta solicitação está diretamente vinculada, se houver',
        blank=True,
        null=True, 
        verbose_name='Etapa vinculada', 
        )
    atividade_vinculada = models.ForeignKey(
        'projetos.Atividade',
        on_delete=models.CASCADE,
        help_text='Selecione a(s) atividade(s) a que esta solicitação está diretamente vinculada.',
        blank=True,
        null=True,
        )
    #== ORÇAMENTOS ==#
    #== Mão de obra e/ou serviços ==#
    orcamento_mo_um = models.ForeignKey(
        orcamento_para_solicitacao_de_fundos,
        on_delete=models.SET_NULL,
        help_text='Selecione o primeiro orçamento de mão de obra três que devem compor a solicitação de fundos. Se não houver, clique em "+" para inserir.',
        blank=True,
        null=True,
        )
    orcamento_mo_dois = models.ForeignKey(
        orcamento_para_solicitacao_de_fundos,
        on_delete=models.SET_NULL,
        help_text='Selecione o segundo orçamento de três que devem compor a solicitação de fundos. Se não houver, clique em "+" para inserir.',
        blank=True,
        null=True,
        )
    orcamento_mo_tres = models.ForeignKey(
        orcamento_para_solicitacao_de_fundos,
        on_delete=models.SET_NULL,
        help_text='Selecione o terceiro orçamento de três que  devem compor a solicitação de fundos. Se não houver, clique em "+" para inserir.',
        blank=True,
        null=True,
        )
    #== Materiais e/ou insumos ==#
    orcamento_mt_um = models.ForeignKey(
        orcamento_para_solicitacao_de_fundos,
        on_delete=models.SET_NULL,
        help_text='Selecione o primeiro orçamento de mão de obra três que devem compor a solicitação de fundos. Se não houver, clique em "+" para inserir.',
        blank=True,
        null=True,
        )
    orcamento_mt_dois = models.ForeignKey(
        orcamento_para_solicitacao_de_fundos,
        on_delete=models.SET_NULL,
        help_text='Selecione o segundo orçamento de três que devem compor a solicitação de fundos. Se não houver, clique em "+" para inserir.',
        blank=True,
        null=True,
        )
    orcamento_mt_tres = models.ForeignKey(
        orcamento_para_solicitacao_de_fundos,
        on_delete=models.SET_NULL,
        help_text='Selecione o terceiro orçamento de três que  devem compor a solicitação de fundos. Se não houver, clique em "+" para inserir.',
        blank=True,
        null=True,
        )
    #== Maquinas e/ou equipamentos ==#
    orcamento_mq_um = models.ForeignKey(
        orcamento_para_solicitacao_de_fundos,
        on_delete=models.SET_NULL,
        help_text='Selecione o primeiro orçamento de mão de obra três que devem compor a solicitação de fundos. Se não houver, clique em "+" para inserir.',
        blank=True,
        null=True,
        )
    orcamento_mq_dois = models.ForeignKey(
        orcamento_para_solicitacao_de_fundos,
        on_delete=models.SET_NULL,
        help_text='Selecione o segundo orçamento de três que devem compor a solicitação de fundos. Se não houver, clique em "+" para inserir.',
        blank=True,
        null=True,
        )
    orcamento_mq_tres = models.ForeignKey(
        orcamento_para_solicitacao_de_fundos,
        on_delete=models.SET_NULL,
        help_text='Selecione o terceiro orçamento de três que  devem compor a solicitação de fundos. Se não houver, clique em "+" para inserir.',
        blank=True,
        null=True,
        )
    cronograma = models.TextField(
        'Cronograma de execução',
        max_length=300,
        help_text='Especifique um cronograma ou período estimado de relaização das atividades com os fundos solicitados.',
        blank=True,
        null=True,
        )
    URGENCIAS = [
        ('Alta', 'ALTA'),
        ('Média', 'MÉDIA'),
        ('Baixa', 'BAIXA'),
    ]
    urgencia = models.CharField(
        'Caráter de urgência',
        max_length=5,
        choices=URGENCIAS,
        help_text='Selecione o caráter de urgência para liberação de fundos.',
        )
    observacoes = models.TextField(
        'Observações',
        help_text='Inclua quaiquer observações que considerar necessário.',
        blank=True,
        null=True,
    )

    def __str__(self):
        return 'SOL' + str(self.id).zfill(6)