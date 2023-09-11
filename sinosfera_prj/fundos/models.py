from datetime import date
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from pessoas.models import CustomUser

#======================================#
#== TABELA DE SOLICITAÇÕES DE FUNDOS ==#
#======================================#

class Item(models.Model):
    """Tabela de inserção de dados de itens de despesa (produtos e serviços)."""
    nome = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text='Insira o nome produto ou serviço.',
    )
    unidade = models.ForeignKey(
        'categorias.Unidade_de_medida',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Selecione a unidade de medida do ítem de despesa no orçamento.',
        verbose_name='Un',
        default='un',
    )
    descricao = models.CharField(
        max_length=80,
        help_text='Inclua uma breve descrição do item de despesa.',
        blank=True,
        null=True,
        verbose_name='Descrição',
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
        max_length=90, 
        blank=True,
        null=True,
        verbose_name='ID Codificada',
        editable=False,
        unique=True,
        ) 

    def save(self, *args, **kwargs):
        self.id_codificada = 'ITE' + str(self.id).zfill(3) + ' ' + str(self.nome) + ' (' + str(self.unidade) + ')'
        super().save(*args, **kwargs)

    # Signal to populate dependable fields correctly when the object is created
    @receiver(post_save, sender='fundos.Item')
    def populate_readonly_fields(sender, instance, created, **kwargs):
        if created:
            instance.id_codificada = 'ITE' + str(instance.id).zfill(3) + ' ' + str(instance.nome) + ' (' + str(instance.unidade) + ')'
            instance.save()  # Save the object again to persist the change

    def __str__(self):
        return str(self.id_codificada)
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Produto ou serviço'
        verbose_name_plural = 'Produtos ou serviços'   


class Pedido(models.Model):
    orcamento = models.ForeignKey(
        'Orcamento',
        on_delete=models.CASCADE,
        help_text='Selecione em que orçamento esse pedido se insere.',
        blank=True,
        null=True,
    )
    tipo = models.ForeignKey(
        'categorias.Categoria_de_despesa',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text='Selecione a categoria de despesa.',
        verbose_name='Tipo de despesa',
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        help_text='Selecione um item para este pedido',
        blank=True,
        null=True,
    )
    especificacao = models.CharField(
        max_length=80,
        help_text='Inclua especificações do item de despesa quando houver especificações técnicas.',
        blank=True,
        null=True,
        verbose_name='Especificação',
        )
    quantidade = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text='Especifique a quantidade que deseja adquirir.',
        verbose_name='QTD',
        default=0,
    )    
    preco_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Especifique o preço unitário do item.',
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
    # ==== Utility fields ==== #
    criado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='pedidos_criados', 
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
        related_name='pedidos_atualizados', 
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

    def save(self, *args, **kwargs):
        self.id_codificada = 'PED' + str(self.id).zfill(3) + '-' + str(self.item) + '(' + str(self.quantidade) + ')' # + ' ' + str(self.item.unidade) + ')' 
        super().save(*args, **kwargs)
        self.subtotal_do_item = self.preco_unitario * self.quantidade
        super().save(*args, **kwargs)

    # Signal to populate id_codificada when the object is created
    @receiver(post_save, sender='fundos.Pedido')
    def populate_id_codificada(sender, instance, created, **kwargs):
        if created:
            # The object is being created, so set id_codificada accordingly
            instance.id_codificada = 'PED' + str(instance.id).zfill(3) + '-' + str(instance.item) + '(' + str(instance.quantidade) + ')'
            instance.subtotal_do_item = instance.preco_unitario * instance.quantidade
            instance.save(update_fields=['subtotal_do_item'])  # Save the object again to persist the change
    
    def __str__(self):
        return str(self.id_codificada)
    

    class Meta:
        ordering = ('id',)
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


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
    arquivos = models.FileField(
        upload_to='fundos/orcamentos', 
        blank=True, 
        null=True,
        verbose_name='Arquivo de orçamento',
        )
    # ==== Utility fields ==== #
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
    id_codificada = models.CharField(
        max_length=60, 
        blank=True,
        null=True,
        verbose_name='ID Codificada',
        editable=False,
        unique=True,
        )

    def save(self, *args, **kwargs):
        if self.empresa_fornecedora:
            self.id_codificada = 'ORC' + str(self.id).zfill(5) + ' - ' + str(self.empresa_fornecedora)[0:30] + '...' + str(self.data)
        elif self.profissional_fornecedor:
            self.id_codificada = 'ORC' + str(self.id).zfill(5) + ' - ' + str(self.profissional_fornecedor)[0:30] + '...' + str(self.data)
        else:
            self.id_codificada = 'ORC' + str(self.id).zfill(5) + ' - fornecedor indeterminado' + ' - ' + str(self.data)
        super().save(*args, **kwargs) 
        self.total_do_orcamento=sum(pedido.subtotal_do_item for pedido in Pedido.objects.filter(orcamento=self))
        super().save(*args, **kwargs)

    # Signal to populate id_codificada and total_do_orcamento when the object is created
    @receiver(post_save, sender='fundos.Orcamento')
    def populate_id_codificada(sender, instance, created, **kwargs):
        if created:
            # The object is being created, so set id_codificada accordingly
            if instance.empresa_fornecedora:
                instance.id_codificada = 'ORC' + str(instance.id).zfill(5) + ' - ' + str(instance.empresa_fornecedora)[0:30] + '...' + str(instance.data)
                instance.save()  # Save the object again to persist the change
            elif instance.profissional_fornecedor:
                instance.id_codificada = 'ORC' + str(instance.id).zfill(5) + ' - ' + str(instance.profissional_fornecedor)[0:30] + '...' + str(instance.data)
                instance.save()  # Save the object again to persist the change
            else:
                instance.id_codificada = 'ORC' + str(instance.id).zfill(5) + ' - fornecedor indeterminado' + ' - ' + str(instance.data)
                instance.save()  # Save the object again to persist the change
            # The object is being created, so set total_do_orcamaneto accordingly
            instance.total_do_orcamento = sum(pedido.subtotal_do_item for pedido in Pedido.objects.filter(orcamento=instance))
            instance.save(update_fields=['total_do_orcamento'])  # Save the object again to persist the change

    def __str__(self):
        return str(self.id_codificada)


    class Meta:
        ordering = ('id',)
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'   


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
    subprojeto_vinculado = models.ManyToManyField(
        'projetos.Subprojeto', 
        help_text='Selecione os subprojetos a que esta solicitação está diretamente vinculada.', 
        blank=True, 
        verbose_name='Subprojeto(s) vinculado(s) à solicitação de fundos', 
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
    # ==== Utility fields ==== #
    criado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='requisicoes_criadas', editable=False,)
    atualizado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='requisicoes_atualizadas', editable=False,)
    criado_em = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    atualizado_em = models.DateTimeField(auto_now=True, blank=True, null=True,)
    id_codificada = models.CharField(
        max_length=60, 
        blank=True,
        null=True,
        verbose_name='ID Codificada',
        editable=False,
        unique=True,
        )

    def save(self, *args, **kwargs):
        self.id_codificada = 'REQ' + str(self.id).zfill(4) 
        super().save(*args, **kwargs)

    # Signal to populate id_codificada when the object is created
    @receiver(post_save, sender='fundos.Requisicao')
    def populate_id_codificada(sender, instance, created, **kwargs):
        if created:
            # The object is being created, so set id_codificada accordingly
            instance.id_codificada = 'REQ' + str(instance.id).zfill(4)
            instance.save()  # Save the object again to persist the change

    def __str__(self):
        return str(self.id_codificada)
    

    class Meta:
        ordering = ('id',)
        verbose_name = 'Requisiçáo de fundos'
        verbose_name_plural = 'Requisições de fundos'
