from datetime import date, datetime
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import AbstractBaseUser, User

#======================================#
#== TABELA DE SOLICITAÇÕES DE FUNDOS ==#
#======================================#


class Item(models.Model):
    """Tabela de inserção de dados de item de orçamento, seja este item serviço, material ou maquinário."""
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
    descricao = models.TextField(
        'Descrição',
        help_text='Inclua uma breve descrição do item quando houver especificações técnicas.',
        blank=True,
        null=True,
    )

    def __str__(self):
        return 'ITE' + str(self.id).zfill(3) + ' ' + str(self.nome) + ' (' + str(self.unidade) + ')'
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Item de compra'
        verbose_name_plural = 'Itens de compra'   

class Orcamento(models.Model):
    """Tabela de inserção de dados dos orçamentos para solicitação de fundos."""
    solicitacao = models.ForeignKey(
        'Solicitacao_de_fundos',
        on_delete=models.SET_NULL,
        help_text='Selecione a solicitação de fundos em que este orçamento se insere.',
        blank=True,
        null=True,
        verbose_name='Solicitação de fundos',
        )
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
    numero_NF = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        help_text='Insira o número da NF após compra confirmada',
    )
    data_NF = models.DateField(
        'Data da NF',
        blank=True,
        null=True,
        help_text='Insira da data de emissão da NF.',
    )
    profissional_fornecedor = models.ForeignKey(
        'pessoas.Pessoa',
        on_delete=models.SET_NULL,
        help_text='Selecione o profissional fornecedor. Senão houver, clieque em "+" para inserir.',
        blank=True,
        null=True,
        )
    numero_RPA = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        help_text='Insira o número do RPS após a compra confirmada',
    )
    data_RPA = models.DateField(
        'Data da NF',
        blank=True,
        null=True,
        help_text='Insira da data de emissão do RPA.',
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
    exclui = models.TextField(
        help_text='Especifique o que não está incluso neste orçamento, quando pertinente.',
        blank=True,
        null=True,
        verbose_name='Não incluso neste orçamento',
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
    

    # def atualiza_valor_total_do_orcamento(self):
    #     self.total_do_orcamento = sum(pedido.total_do_item for pedido in self.inclui.all())

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.atualiza_valor_total_do_orcamento()

    def __str__(self):
        if self.empresa_fornecedora:
            return 'ORC' + str(self.id).zfill(5) + ' - ' + str(self.empresa_fornecedora)
        elif self.profissional_fornecedor:
            return 'ORC' + str(self.id).zfill(5) + ' - ' + str(self.profissional_fornecedor)
        else:
            'ORC' + str(self.id).zfill(5) + ' - fornecedor indeterminado'


    class Meta:
        ordering = ('id',)
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'   

class Pedido_de_item(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Item solicitado',
        )
    quantidade = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text='Especifique a quantidade que deseja adquirir considerando a unidade de medida do item.',
        verbose_name='Qtd.',
    )    
    preco_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Especifique o preço unitário do item de orçamento.',
        verbose_name='Preço unitário',
    )
    total_do_pedido_do_item = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        default=0,
        verbose_name='Subtotal do item',
    )
    orcamento = models.ForeignKey(
        'Orcamento',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    def save(self, *args, **kwargs):
        self.total_do_item = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return 'PED' + str(self.id).zfill(6) + ' - ' + str(self.item.nome)
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Pedido de item'
        verbose_name_plural = 'Pedidos de itens'

    
    #calculo do valor do orçamento
    def save(self, *args, **kwargs):
        self.total_do_pedido_do_item = self.preco_unitario * self.quantidade
        self.orcamento.total_do_orcamento += self.total_do_pedido_do_item # FIXME: object has no attribute total_do_orcamento
        self.orcamentorcamento.save()
        return super(Pedido_de_item, self).save(*args, **kwargs)



class Solicitacao_de_fundos(models.Model):
    """Tabela de inserção de dados para solicitação de fundos."""
    fundo_solicitado = models.ForeignKey(
        'categorias.Fundo',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Fundo de financiamento',
    )
    data = models.DateField(
        'Data da solicitação',
        default=date.today, 
        blank=True,
        null=True, 
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
    projeto_vinculado = models.ForeignKey(
        'projetos.Projeto', 
        on_delete=models.SET_NULL, 
        help_text='Selecione o projeto a que esta solicitação está diretamente vinculada.',
        blank=True, 
        null=True, 
        verbose_name='Projeto vinculado à solicitação de fundos', 
        )
    instituicao_solicitante = models.ForeignKey(
        'instituicoes.Instituicao',
        on_delete=models.SET_NULL,
        verbose_name='Insituição solicitante',
        blank=True,
        null=True,
    )    
    objetivo_especifico_vinculado = models.ManyToManyField(
        'projetos.Objetivo_especifico_de_projeto', 
        help_text='Selecione o objetivo específico a que esta solicitação está diretamente vincula.', 
        blank=True, 
        verbose_name='Objetivo(s) específico(s) vinculado(s) à solicitação de fundos', 
        )
    etapa_vinculada = models.ManyToManyField(
        'projetos.Etapa', 
        help_text='Selecione a(s) etapa(s) a que esta solicitação está diretamente vinculada, se houver',
        blank=True,
        verbose_name='Etapa(s) vinculada(s)', 
        )
    atividade_vinculada = models.ManyToManyField(
        'projetos.Atividade',
        help_text='Selecione a(s) atividade(s) a que esta solicitação está diretamente vinculada.',
        blank=True,
        )
    ur_vinculada = models.ManyToManyField(
        'locais.Unidade_de_referencia',
        help_text='Selecione uma ou mais URs destino dos fundos dessa solicitação, se houver.',
        blank=True,
        verbose_name='UR(s) vinculada(s) à solicitação de fundos',
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
    arquivos = models.FileField(
        upload_to='fundos/solicitacoes', 
        blank=True, 
        null=True,
    )

    def __str__(self):
        return 'SOL' + str(self.id).zfill(6)
    

    class Meta:
        ordering = ('id',)
        verbose_name = 'Solicitação de fundo'
        verbose_name_plural = 'Solicitações de fundos'