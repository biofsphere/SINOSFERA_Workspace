from datetime import date, datetime
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from pessoas.models import CustomUser
import threading

_thread_locals = threading.local()

#======================================#
#== TABELA DE SOLICITAÇÕES DE FUNDOS ==#
#======================================#


class Item(models.Model):
    """Tabela de inserção de dados de item de despesa no orçamento, seja este item serviço, material ou maquinário."""
    orcamento = models.ForeignKey(
        'Orcamento',
        related_name='itens',
        verbose_name='Orçamento a que esta compra pertence',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text='Selecione o orçamento a que esta compra de itens de despesa faz parte.',
    )
    TIPOS_DE_DESPESA = [
        ('MOB', 'Mão de obra ou serviços'),
        ('REF', 'Refeições ou alimentação'),
        ('TRA', 'Frete ou transporte'),
        ('FMA', 'Ferramentas manuais'),
        ('FMO', 'Ferramentas motorizadas'),
        ('MTC', 'Materiais de construção'),
        ('INS', 'Materiais escolares'),
        ('AGR', 'Insumo agropecuário'),
        ('EQU', 'Equipamentos de TI'),
        ('MOV', 'Móveis'),
        ('PCO', 'Peças de comunicação'),
        ('ROA', 'Roupas ou acessórios'),
        ('OUT', 'Outros'),
        ]
    tipo = models.CharField(
        max_length=3,
        choices=TIPOS_DE_DESPESA,
        blank=True,
        null=True,
        help_text='Selecione o tipo mais adequado de despesa.',
        verbose_name='Tipo de despesa',
    )
    nome = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text='Insira o nome ou título do serviço, material ou maquinário (item de despesa no orçamento)',
    )
    descricao = models.CharField(
        max_length=80,
        help_text='Inclua uma breve descrição do item de despesa quando houver especificações técnicas.',
        blank=True,
        null=True,
        verbose_name='Descrição',
        )
    unidade = models.ForeignKey(
        'categorias.Unidade_de_medida',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Selecione a unidade de medida do ítem de despesa no orçamento.',
        verbose_name='UN',
    )
    quantidade = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text='Especifique a quantidade que deseja adquirir considerando a unidade de medida do item de despesa.',
        verbose_name='QTD',
        default=0,
    )    
    preco_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Especifique o preço unitário do item de orçamento.',
        verbose_name='Preço Un.',
        default=0,
    )
    subtotal_do_item = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        default=0,
        verbose_name='Subtotal',
    )
    # ==== Utility fields == #
    criado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='itens_criados', 
        editable=False,
        )
    criado_em = models.DateTimeField(
        auto_now_add=True, 
        blank=True, 
        null=True,
        )
    atualizado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='itens_atualizados', 
        editable=False,
        )
    atualizado_em = models.DateTimeField(
        auto_now=True, 
        blank=True, 
        null=True,)
    id_codificada = models.CharField(
        max_length=60, 
        blank=True,
        null=True,
        verbose_name='ID Codificada',
        editable=False,
        unique=True,
        ) 

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     # self.update_related_orcamento_total()

    # def update_related_orcamento_total(self):
    #     if self.orcamento:
    #         self.orcamento.update_total_do_orcamento()

    def save(self, *args, **kwargs):
        self.id_codificada = 'ITE' + str(self.id).zfill(3) + ' ' + str(self.nome) + ' (' + str(self.unidade) + ')'
        self.subtotal_do_item = self.preco_unitario * self.quantidade
        super().save(*args, **kwargs)

    # Signal to populate subtotal_do_item correctly when the object is created
    @receiver(post_save, sender='fundos.Item')
    def populate_readonly_fields(sender, instance, created, **kwargs):
        if created:
            # The object is being created, so set subtotal_do_item and id_codificada accordingly
            instance.id_codificada = 'ITE' + str(instance.id).zfill(3) + ' ' + str(instance.nome) + ' (' + str(instance.unidade) + ')'
            instance.subtotal_do_item = instance.preco_unitario * instance.quantidade
            instance.save(update_fields=['subtotal_do_item', 'id_codificada'])  # Save the object again to persist the change

    # def get_item_id(self):
    #     return 'ITE' + str(self.id).zfill(3) + ' ' + str(self.nome) + ' (' + str(self.unidade) + ')'
    # get_item_id.short_description = 'ID Codificada'  # Set the custom column header name

    def __str__(self):
        return self.id_codificada
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Produto ou serviço'
        verbose_name_plural = 'Produtos ou serviços'   


class Orcamento(models.Model):
    """Tabela de inserção de dados dos orçamentos para solicitação de fundos."""
    requisicao = models.ForeignKey(
        'Requisicao',
        on_delete=models.SET_NULL,
        help_text='Selecione a Requisição de Fundos em que este Orçamento faz parte.',
        blank=True,
        null=True,
        verbose_name='Requisição de Fundos',
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
        help_text='Especifique por quantos dias este orçamento é válido.',
        blank=True,
        null=True,
        default=30,
        verbose_name='Validade do orçamento',
    )
    forma_de_garantia = models.CharField(
        max_length=200,
        help_text='Explicite a forma e tempo de garantia do fornecedor.',
        blank=True,
        null=True,
        verbose_name='Forma e tempo de garantia do fornecedor'
    )
    dados_para_pagamento = models.TextField(
        'Dados para pagamento',
        help_text='Inclua os dados para pagamento deste orçamento conforme preferência do fornecedor (Pix, dados para depósito, etc.).',
        blank=True,
        null=True,
    )
    exclui = models.TextField(
        help_text='Especifique o que não está incluso neste orçamento, caso seja relevante esclarecer.',
        blank=True,
        null=True,
        verbose_name='O que não está incluso neste orçamento',
    )
    observacoes = models.TextField(
        'Observações adicionais',
        help_text='Insira quaisquer observações adicionais que considerar pertinente sobre esse orçamento.',
        blank=True,
        null=True,
    )
    total_do_orcamento = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        editable=False,
        verbose_name='Valor total do orçamento',
        )
    criado_por = models.ForeignKey(
        CustomUser, 
        related_name='criou_orcamento', 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        )
    modificado_por = models.ForeignKey(
        CustomUser, 
        related_name='modificou_orcamento', 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to='fundos/orcamentos', 
        blank=True, 
        null=True,
        verbose_name='Arquivo de orçamento',
        )
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # Save the Orcamento object first
    #     self.update_total_do_orcamento()

    # def update_total_do_orcamento(self):
    #     total = self.itens.aggregate(Sum('subtotal_do_item'))['subtotal_do_item__sum']
    #     self.total_do_orcamento = total if total is not None else 0
    #     self.save(update_fields=['total_do_orcamento'])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 
        self.total_do_orcamento=sum(item.subtotal_do_item for item in self.itens.all())
        super().save(*args, **kwargs)

    # # Signal to populate total_do_orcamento correctly when the object is created
    # @receiver(post_save, sender='fundos.Orcamento')
    # def populate_total_do_orcamento(sender, instance, created, **kwargs):
    #     if created:
    #         # The object is being created, so set total_do_orcamaneto accordingly
    #         instance.total_do_orcamento = sum(item.subtotal_do_item for item in instance.itens.all())
    #         instance.save(update_fields=['total_do_orcamento'])  # Save the object again to persist the change
    

    def get_item_id(self):
        if self.empresa_fornecedora:
            return 'ORC' + str(self.id).zfill(5) + ' - ' + str(self.empresa_fornecedora)[0:30] + '...' + str(self.data)
        elif self.profissional_fornecedor:
            return 'ORC' + str(self.id).zfill(5) + ' - ' + str(self.profissional_fornecedor)[0:30] + '...' + str(self.data)
        else:
            return 'ORC' + str(self.id).zfill(5) + ' - fornecedor indeterminado' + ' - ' + str(self.data)
    get_item_id.short_description = 'ID Codificada'  # Set the custom column header name

    def __str__(self):
        if self.empresa_fornecedora:
            return 'ORC' + str(self.id).zfill(5) + ' - ' + str(self.empresa_fornecedora)[0:30] + '...'
        elif self.profissional_fornecedor:
            return 'ORC' + str(self.id).zfill(5) + ' - ' + str(self.profissional_fornecedor)[0:30] + '...'
        else:
            return 'ORC' + str(self.id).zfill(5) + ' - fornecedor indeterminado'


    class Meta:
        ordering = ('id',)
        verbose_name = 'Orçamento de fornecedor(a)'
        verbose_name_plural = 'Orçamentos de fornecedores(as)'   


class Requisicao(models.Model):
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
        upload_to='fundos/requisicoes', 
        blank=True, 
        null=True,
        verbose_name='Arquivo de requisição de fundos',
    )
    criado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='requisicoes_criadas', editable=False,)
    atualizado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='requisicoes_atualizadas', editable=False,)
    criado_em = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    atualizado_em = models.DateTimeField(auto_now=True, blank=True, null=True,)

    def get_item_id(self):
        return 'REQ' + str(self.id).zfill(3) + ' ' + str(self.data) + ' ' + str(self.projeto_vinculado)[0:30]
    get_item_id.short_description = 'ID Codificada'  # Set the custom column header name

    def __str__(self):
        return 'REQ' + str(self.id).zfill(4)
    

    class Meta:
        ordering = ('id',)
        verbose_name = 'Requisiçáo de fundos'
        verbose_name_plural = 'Requisições de fundos'
