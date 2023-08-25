from datetime import date, datetime
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

#######################################################
### TABELAS DE PROGRAMAS DE MOBILIZAÇÃO DE PROJETOS ###
#######################################################

#==============#
#== PROGRAMA ==#
#==============#

class Programa(models.Model):
    """Tabela de inserção de dados sobre programas de mobilização de projetos, tais como o VerdeSinos. Não se trata de Programas de Ações Prioritárias, mas de um nível abaixo destest, onde se encaixam programas regionais que abordam um ou mais as ações prioritárias previstas nestes Programas de Ações Prioritárias dos Planos Plurianuais."""
    plano_vinculado_ao_programa = models.ForeignKey(
        'planos.Plano',
        on_delete=models.SET_NULL,
        related_name='programas_vinculados_ao_plano',
        verbose_name='Plano vinculado a este Programa',
        blank=True,
        null=True,
        help_text='Selecione o Plano a que este Programa se vincula.',
    )
    nome = models.CharField(
        'Nome ou título do Programa',
        max_length=150,
        help_text='Defina um nome curto para o Programa.',
        blank=True,
        null=True,    
    )
    objetivo_geral_do_programa = models.TextField(
        'Objetivo geral do Programa',
        help_text='Descreva de modo geral o que o Programa pretente alcançar na sociedade e no meio ambiente.',
        blank=True,
        null=True,
        )
    resumo_descritivo_do_programa = models.TextField(
        'Resumo descritivo do Programa',
        help_text='Descreva de modo geral o que é, quem está envolvido, onde se dará a execução, quando deverá ocorrer a execução, como e porque o Programa será executado.',
        blank=True,
        null=True,
        )
    fundos_de_execucao_do_programa = models.TextField(
        'Fundos de execução do Programa',
        help_text='Descreva brevemente as fontes de recursos para execução deste Programa.',
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
    prazo_de_execucao_do_programa =  models.CharField(
        max_length=2,
        choices=ESCOPOS_TEMPORAIS,
        help_text='Selecione o prazo estabelecido para execução completa deste Programa',
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
    escopo_geografico_do_programa =  models.CharField(
        max_length=3,
        choices=ESCOPOS_GEOGRAFICOS,
        help_text='Selecione o escopo geográfico do Programa',
        blank=True,
        null=True,  
    )
    #== Ancoragens do Programa ==#
    municipio_ancora_do_programa = models.ForeignKey(
        'locais.Municipio',
        on_delete=models.SET_NULL,
        verbose_name='Município âncora do Programa',
        help_text='Selecione o município cosiderado a sede ou âncora deste programa.', 
        blank=True,
        null=True, 
        )
    instituicao_ancora_do_programa = models.ForeignKey(
        'instituicoes.Instituicao',
        on_delete=models.SET_NULL,
        verbose_name='Instituição âncora do Programa',
        help_text='Selecione a Instituição considerada a proponente principal ou a âncora do Programa',
        blank=True,
        null=True,
        )
    pessoa_ancora_do_programa = models.ForeignKey(
        'pessoas.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Especifique a pessoa âncora, ou coordenadora deste programa, se houver.', 
        blank=True,
        null=True,
        verbose_name='Coordenador geral', 
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to='programas',
        blank=True, 
        null=True,
        )

    @property
    def projetos_relacionados_ao_programa(self):
        """Chama todos os projetos vinculados ao Programa usando o ralated_name=projetos_vinculados_ao_programa utilizado no model Projeto"""
        return self.projetos_vinculados_ao_programa.all()

    def get_absolute_url(self):
        """Traz a URL de perfil do Programa."""
        return reverse('programa-detalhe', args=[str(self.id)])

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'PRG' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'


#===================================================================#
#== DIRETRIZES ESPECÍFICAS DO PROGRAMA DE MOBILIZAÇÃO DE PROJETOS ==#
#===================================================================#

class Diretriz_especifica_de_programa(models.Model):    
    """Tabela de inserção de dados sobre as diretrizes específicas do programa de mobilização de projetos."""
    programa_vinculado_a_diretriz_especifica = models.ForeignKey(
        Programa, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o Programa ao qual a diretriz específica está vinculado.', 
        blank=True, 
        null=True, 
        verbose_name='Programa vinculado', 
        )
    nome = models.CharField(
        'Nome ou título da diretriz específica', 
        help_text='Defina um título ou nome curto para a diretriz específica do Programa.', 
        max_length=120,
        blank=True,
        null=True,
        )
    descricao_da_diretriz_especifica = models.TextField(
        'Descrição da diretriz específica do programa', 
        help_text='Descreva a diretriz específica de forma genérica objetivando nortear os projetos que se vincularão a ela.', 
        max_length=600,
        blank=True,
        null=True,
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'DIR' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Diretriz específica'
        verbose_name_plural = 'Diretrizes específicas'