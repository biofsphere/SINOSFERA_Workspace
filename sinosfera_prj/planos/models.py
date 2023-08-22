from datetime import date, datetime
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User

###############################
### TABELAS DE PLANEJAMENTO ###
###############################

#===========#
#== PLANO ==#
#===========#

class Plano(models.Model):
    """Tabela de inserção de dados sobre planos geralmente plurianuais, regionais ou municipais. Porém podem ser inseridos outros escopos temporais e geográficos."""
    nome = models.CharField(
        'Nome ou título do Plano', 
        help_text='Defina um nome curto para o Plano.', 
        max_length=120,
        blank=True,
        null=True,
        )
    objetivo_geral_do_plano = models.TextField(
        'Objetivo geral do Plano', 
        help_text='Descreva de modo geral o que o Plano pretende alcançar na sociedade e no meio ambiente.', 
        blank=True,
        null=True,
        )
    resumo_descritivo = models.TextField(
        'Resumo descritivo do Plano',
        help_text='Descreva de modo geral o que é, quem está envolvido, onde se dará a execução, quando deverá ocorrer a execução, como e porque o Plano será executado.',
        blank=True,
        null=True,
        )
    fundos_de_execucao = models.TextField(
        'Fundos de execução do Plano',
        help_text='Descreva brevemente as fontes de recursos para execução dest Plano.',
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
    prazo_de_execucao =  models.CharField(
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
    escopo_geografico =  models.CharField(
        max_length=3,
        choices=ESCOPOS_GEOGRAFICOS,
        help_text='Selecione o escopo geográfico do Plano',
        blank=True,
        null=True,  
    )
    #== Ancoragens do Plano ==#
    municipio_ancora_do_plano = models.ForeignKey(
        'locais.Municipio', 
        verbose_name='Município âncora do Plano',
        help_text='Selecione o município cosiderado a sede ou âncora deste plano.', 
        blank=True, 
        )
    instituicao_ancora_do_plano = models.ForeignKey(
        ''
        )

    coordenador = models.ForeignKey(
        'people.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Especifique a pessoa âncora, ou coordenadora deste plano, se houver.', 
        blank=True,
        null=True,
        verbose_name='Coordenador geral', 
        )

    bh = models.OneToOneField(
        'places.Bacia_hidrografica',
        on_delete=models.SET_NULL, 
        verbose_name='Bacia hidrográfica', 
        help_text='Selecione a bacia hidrográfica quando se tratar de Plano de Bacia.', 
        blank=True, 
        null=True, 
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    arquivos = models.FileField(
        upload_to=r'plans_media\pla_media', 
        blank=True, 
        null=True,
        )

    def get_absolute_url(self):
        """Traz a URL de perfil do Plano Plurianual."""
        return reverse('plano-detalhe', args=[str(self.id)])

    def __str__(self):
        return 'PLA' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Plano Plurianual'
        verbose_name_plural = '07 - Planos plurianuais'



#====================================#
#== PROGRAMA DE AÇÕES PRIORITÁRIAS ==#
#====================================#

class Programa(models.Model):
    nome = models.CharField(
        'Nome ou título', 
        help_text='Defina um nome para o program de ações ou projeto de maior escopo dentro do plano plurianual.', 
        max_length=120,
        blank=True,
        null=True,
        )

    obj_geral = models.TextField(
        'Objetivo geral', 
        help_text='Descreva de modo geral o que o programa de ações deseja alcançar.', 
        max_length=600,
        blank=True,
        null=True,
        )
    
    coordenador = models.ForeignKey(
        'people.Pessoa',  
        on_delete=models.SET_NULL, 
        help_text='Especifique a pessoa âncora ou coordenadora do programa de ações prioritárias.', 
        blank=True, 
        null=True,
        verbose_name='Coordenador geral',  
        )

    plano_vinculado = models.ForeignKey(
        Plano, 
        on_delete=models.SET_NULL, 
        help_text='Especifique a qual plano plurianual este programa de ações prioritárias está vinculado.', 
        blank=True,
        null=True, 
        verbose_name='Plano plurianual vinculado',  
        ) 

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)  

    arquivos = models.FileField(
        upload_to=r'plans_media\prg_media', 
        blank=True, 
        null=True,
        )

    def get_absolute_url(self):
        """Traz a URL de perfil do Programa."""
        return reverse('programa-detalhe', args=[str(self.id)])

    def __str__(self):
        return 'PRG' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Programa de ações'
        verbose_name_plural = '08 - Programas de ações'



#========================#
#== AÇÕES PRIORITÁRIAS ==#
#========================#

class Acao(models.Model):
    nome = models.CharField(
        'Nome ou título', 
        help_text='Defina um nome ou título para a ação prioritária.', 
        max_length=120,
        blank=True,
        null=True,
        )

    obj_geral = models.TextField(
        'Objetivo geral', 
        help_text='Descreva de modo geral o que esta ação prioritária deseja alcançar.', 
        max_length=600,
        blank=True,
        null=True,
        )
    
    coordenador = models.ForeignKey(
        'people.Pessoa',  
        on_delete=models.SET_NULL, 
        help_text='Especifique a pessoa âncora ou coordenadora da ação prioritária, se houver.',  
        blank=True, 
        null=True, 
        verbose_name='Coordenador geral da ação', 
        )

    programa_vinculado = models.ForeignKey(
        Programa, 
        on_delete=models.SET_NULL, 
        help_text='Especifique a que programa de ações a ação está vinculada.', 
        blank=True, 
        null=True, 
        verbose_name='Programa de ações vinculado', 
        )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    arquivos = models.FileField(
        upload_to=r'plans_media\aca_media', 
        blank=True, 
        null=True,
        )

    def get_absolute_url(self):
        """Traz a URL de perfil da Ação Prioritária."""
        return reverse('acao-detalhe', args=[str(self.id)])

    def __str__(self):
        return 'ACA' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Ação prioritária'
        verbose_name_plural = '09 - Ações prioritárias'
