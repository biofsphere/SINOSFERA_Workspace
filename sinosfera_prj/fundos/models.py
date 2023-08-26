from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User

#======================================#
#== TABELA DE SOLICITAÇÕES DE FUNDOS ==#
#======================================#


class Item(models.Model):
    """Tabela de inserção de dados de item de orçamento, seja este item serviço, material ou maquinário."""
    # orcamento = models.ForeignKey(
    #     'Orcamento_para_solicitacao_de_fundos',
    #     on_delete=models.CASCADE,
    #     related_name='itens_orcados',
    #     help_text='Selecione o orçamento no qual este item pertence.',
    #     blank=True,
    #     null=True,
    # )
    nome = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        help_text='Insira o nome to serviço, material ou maquinário (item de orçamento)',
    )
    TIPOS_DE_ITENS = [
        ('MO', 'Mão de obra ou serviço'),
        ('MT', 'Materiais ou insumo'),
        ('MQ', 'Máquina ou equipamento'),
        ]
    tipo = models.CharField(
        max_length=2,
        choices=TIPOS_DE_ITENS,
        blank=True,
        null=True,
        help_text='Selecione o tipo mais adequado de item de orçamento.',
        verbose_name='Tipo de item',
    )
    unidade = models.ForeignKey(
        'categorias.Unidade_de_medida',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Selecione a unidade de medida do ítem de orçamento.',
        verbose_name='Un.',
    )
    quantidade = models.PositiveIntegerField(
        help_text='Especifique a quantidade que deseja adquirir considerando a unidade de medida especificada.',
        verbose_name='Qtd.',
    )    
    preco_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Especifique o preço unitário do item de orçamento.',
        verbose_name='Preço unitário',
    )
    total_do_item = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        verbose_name='Total do item',
    )

    def save(self, *args, **kwargs):
        self.total_do_item = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return 'ITE' + str(self.id).zfill(6)
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Item de orçamento'
        verbose_name_plural = 'Itens de orçamento'   


class Orcamento(models.Model):
    """Tabela de inserção de dados dos orçamentos para solicitação de fundos."""
    # solicitacao_de_fundos = models.ForeignKey(
    #     'solicitacao_de_fundos',
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     null=True,
    #     help_text='Selecione a solicitação de fundos na qual este orçamento pertence.',
    # )
    data = models.DateField(
        help_text='Seleciona a data do orçamento fornecido.',
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
    inclui = models.ManyToManyField(
        Item,
        help_text='Selecione os itens inclusos neste orçamento',
        blank=True,
        null=True,
    )
    exclui = models.TextField(
        help_text='Descreva o que o orçameto não inclui, quando pertinente.',
        blank=True,
        null=True,
        verbose_name='Não incluso',
    )
    validade = models.PositiveIntegerField(
        help_text='Especifique por quantos dias orçamento é válido.',
        blank=True,
        null=True,
    )
    forma_de_garantia = models.CharField(
        max_length=200,
        help_text='Explicite a forma e tempo de garantia do fornecedor.',
        blank=True,
        null=True,
    )
    total_do_orcamento = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        editable=False,
        )
    dados_para_pagamento = models.TextField(
        'Dados para pagamento',
        help_text='Inclua os dados para pagamento deste orçamento conforme preferência do fornecedor.',
        blank=True,
        null=True,
    )
    observacoes = models.TextField(
        'Observações',
        help_text='Insira quaisquer observações que considerar pertinente sobre esse orçamento.',
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

    def atualiza_valor_total_do_orcamento(self):
        self.total_do_orcamento = sum(item.total_do_item for item in self.itens.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.atualiza_valor_total_do_orcamento()

    def __str__(self):
        return 'ORC' + str(self.id).zfill(5)


    class Meta:
        ordering = ('id',)
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'   


class Solicitacao_de_fundos(models.Model):
    """Tabela de inserção de dados para solicitação de fundos."""
    data = models.DateField(
        'Data da solicitação',
        default=date.today, 
        blank=True,
        null=False, 
        )
    municipio = models.ForeignKey(
        'locais.Municipio',
        on_delete=models.SET_NULL,
        help_text='Selecione o município para onde irão os fundos',
        blank=True,
        null=True,
        verbose_name='Município solicitante',
        )
    responsavel_pelo_preenchimento = models.ForeignKey(
        'pessoas.Pessoa',
        on_delete=models.SET_NULL,
        help_text='Selecione a pessoa responsável pelo preenchimento desta solicitação.',
        blank=True,
        null=True,
        verbose_name='Responsável pelo preenchimento',
        )
    # == VÍNCULOS DA ATIVIDADE == #
    ur_vinculada = models.OneToOneField(
        'locais.Unidade_de_referencia',
        on_delete=models.SET_NULL,
        help_text='Selecione a UR a que esta solicitação está diretamente vinculada, se houver.',
        blank=True,
        null=True,
        verbose_name='UR vinculada à solicitação de fundos',
        )    
    projeto_vinculado = models.ForeignKey(
        'projetos.Projeto', 
        on_delete=models.SET_NULL, 
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
    orcamentos = models.ManyToManyField(
        Orcamento,
        help_text='Selecione três orçamentos para cada tipo de orçamento levantado.',
        blank=True,
        null=True,
    )
    total_da_solicitacao = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        editable=False,
        )
    observacoes = models.TextField(
        'Observações',
        help_text='Inclua quaiquer observações que considerar necessário.',
        blank=True,
        null=True,
    )

    def atualiza_valor_total_da_solicitacao(self):
        self.total_da_solicitacao = sum(orcamento.total_do_orcamento for orcamento in self.orcamentos.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.atualiza_valor_total_da_solicitacao()

    def __str__(self):
        return 'SOL' + str(self.id).zfill(6)