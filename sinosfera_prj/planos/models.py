from datetime import date, datetime
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


#===========#
#== PLANO ==#
#===========#

class Plano(models.Model):
    """Tabela de inserção de dados sobre planos geralmente plurianuais, regionais ou municipais. Porém podem ser inseridos outros escopos temporais e geográficos."""
    categoria = models.ForeignKey(
        'categorias.Categoria_de_plano',
        on_delete=models.SET_NULL,
        help_text='Selecione uma categoria para este plano. Se não existir, insira uma categoria nova clicando em "+".',
        blank=True,
        null=True,
        )
    nome = models.CharField(
        'Nome ou título do Plano', 
        help_text='Defina um nome curto para o Plano.', 
        max_length=150,
        blank=True,
        null=True,
        )
    objetivo_geral_do_plano = models.TextField(
        'Objetivo geral do Plano', 
        help_text='Descreva de modo geral o que o Plano pretende alcançar na sociedade e no meio ambiente.', 
        blank=True,
        null=True,
        )
    resumo_descritivo_do_plano = models.TextField(
        'Resumo descritivo do Plano',
        help_text='Descreva de modo geral o que é, quem está envolvido, onde se dará a execução, quando deverá ocorrer a execução, como e porque o Plano será executado.',
        blank=True,
        null=True,
        )
    fundos_de_execucao_do_plano = models.TextField(
        'Fundos de execução do Plano',
        help_text='Descreva brevemente as fontes de recursos para execução deste Plano.',
        blank=True,
        null=True,
        )
    ESCOPOS_TEMPORAIS = [
        ('ML', 'MUITO LONGO (mais de 8 anos)'),
        ('L', 'LONGO (de 4 a 8 anos)'),
        ('M', 'MÉDIO (de dois a 4 anos)'),
        ('C', 'CURTO (de 1 a dois anos)'),
        ('MC', 'MUITO CURTO (menos de 1 ano)'),
    ]
    prazo_de_execucao_do_plano =  models.CharField(
        max_length=2,
        choices=ESCOPOS_TEMPORAIS,
        help_text='Selecione o prazo estabelecido para execução completa deste Plano',
        blank=True,
        null=True,
    )
    ESCOPOS_GEOGRAFICOS = [
        ('NAC', 'Nacional'),
        ('MRE', 'Macroregional'),
        ('EST', 'Estadual'),
        ('MIC', 'Microregional'),
        ('MUN', 'Municipal'),
        ('LOC', 'Local'),
    ]
    escopo_geografico_do_plano =  models.CharField(
        max_length=3,
        choices=ESCOPOS_GEOGRAFICOS,
        help_text='Selecione o escopo geográfico do Plano',
        blank=True,
        null=True,  
    )
    #== Ancoragens do Plano ==#
    municipio_ancora_do_plano = models.ForeignKey(
        'locais.Municipio',
        on_delete=models.SET_NULL,
        verbose_name='Município âncora do Plano',
        help_text='Selecione o município cosiderado a sede ou âncora deste plano.', 
        blank=True,
        null=True, 
        )
    instituicao_ancora_do_plano = models.ForeignKey(
        'instituicoes.Instituicao',
        on_delete=models.SET_NULL,
        verbose_name='Instituição âncora do Plano',
        help_text='Selecione a Instituição considerada a proponente principal ou a âncora do Plano',
        blank=True,
        null=True,
        )
    pessoa_ancora_do_plano = models.ForeignKey(
        'pessoas.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Especifique a pessoa âncora, ou coordenadora deste plano, se houver.', 
        blank=True,
        null=True,
        verbose_name='Coordenador geral', 
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to='planos',
        blank=True, 
        null=True,
        )
    
    @property
    def programas_relacionados_ao_plano(self):
        """Chama todos os programas vinculados ao plano usando o ralated_name=programas_vinculados_ao_plano utilizado no model Programa"""
        return self.programas_vinculados_ao_plano.all()

    def get_absolute_url(self):
        """Traz a URL de perfil do Plano."""
        return reverse('plano-detalhe', args=[str(self.id)])

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'PLA' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Plano plurianual'
        verbose_name_plural = 'Planos plurianuais'



#====================================#
#== PROGRAMA DE AÇÕES PRIORITÁRIAS ==#
#====================================#

class Programa_de_acoes_prioritarias(models.Model):
    """Tabela de inserção de dados sobre os programas de ações prioritárias dos planos plurianuais."""
    plano_vinculado_ao_programa_de_acoes_prioritarias = models.ForeignKey(
        Plano, 
        on_delete=models.SET_NULL, 
        help_text='Especifique a qual plano plurianual este programa de ações prioritárias está vinculado.', 
        blank=True,
        null=True, 
        verbose_name='Plano vinculado',  
        )
    nome = models.CharField(
        'Nome ou título do programa de ações prioritárias', 
        help_text='Defina um nome ou título curto para o program de ações prioritárias do plano.', 
        max_length=120,
        blank=True,
        null=True,
        )
    objetivo_geral_do_programa_de_acoes_prioritarias = models.TextField(
        'Objetivo geral do programa de ações prioritárias', 
        help_text='Descreva de modo geral o que o programa de ações deseja alcançar.', 
        max_length=600,
        blank=True,
        null=True,
        )
    coordenador = models.ForeignKey(
        'pessoas.Pessoa',  
        on_delete=models.SET_NULL, 
        help_text='Selecione uma pessoa âncora ou coordenadora do programa de ações prioritárias.', 
        blank=True, 
        null=True,
        verbose_name='Coordenador geral do programa de ações prioritárias',  
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'PAP' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Programa de ações prioritárias'
        verbose_name_plural = 'Programas de ações prioritárias'


#========================#
#== AÇÕES PRIORITÁRIAS ==#
#========================#

class Acao_prioritaria(models.Model):
    """Tabela de inserção de dados sobre as ações prioritárias dos programas de ações prioritárias dos planos plurianuais."""
    programa_de_acoes_prioritarias_vinculado = models.ForeignKey(
        Programa_de_acoes_prioritarias, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o programa de ações prioritárias a esta ação está vinculada.', 
        blank=True, 
        null=True, 
        verbose_name='Programa de ações vinculado', 
        )
    nome = models.CharField(
        'Nome ou título da ação prioritária', 
        help_text='Defina um nome ou título curto para a ação prioritária.', 
        max_length=120,
        blank=True,
        null=True,
        )
    objetivo_geral = models.TextField(
        'Objetivo geral da ação prioritária', 
        help_text='Descreva de modo geral o que esta ação prioritária deseja alcançar.', 
        max_length=600,
        blank=True,
        null=True,
        )
    coordenador = models.ForeignKey(
        'pessoas.Pessoa',  
        on_delete=models.SET_NULL, 
        help_text='Selecione a pessoa âncora ou coordenadora desta ação prioritária, se houver.',  
        blank=True, 
        null=True, 
        verbose_name='Coordenador geral da ação prioritária', 
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'APR' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Ação prioritária'
        verbose_name_plural = 'Ações prioritárias'
