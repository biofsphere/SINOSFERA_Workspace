

from datetime import date, datetime
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models
from email.policy import default
from django.core.validators import RegexValidator

#########################
### TABELAS DE LOCAIS ###
#########################

#=================#
#== MICROBACIAS ==#
#=================#

class Microbacia(models.Model):
    nome = models.CharField( 
        'Nome da microbacia hidrográfica',
        help_text='Insira o nome da microbacia hidrográfica.',
        max_length=80,
        blank=True,
        null=True,
        unique=True,
        )

    def __str__(self): 
        return 'MBH' + str(self.id).zfill(3) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Microbracia'
        verbose_name_plural = '03 - Microbacias'



#================#
#== MUNICÍPIOS ==#
#================#

class Municipio(models.Model):
    nome = models.CharField(
        'Nome do município',
        help_text='Insira o nome do município.',
        max_length=80,
        blank=True,
        null=True,
        unique=True,
    )

    def __str__(self):
        return 'MUN' + str(self.id).zfill(3) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Município'
        verbose_name_plural = '04 - Municípios'


#============================#
#== UNIDADES DE REFERÊNCIA ==#
#============================#

class Unidade_de_referencia(models.Model):
    nome = models.CharField(
        'Nome da unidade de referência', 
        help_text='Insira um nome ou título para a unidade de referência', 
        default='', 
        unique=True, 
        max_length=120,
        blank=True,
        null=True,
        )

    proprietario_pf = models.ForeignKey(
        'pessoas.Pessoa',   
        on_delete=models.SET_NULL, 
        help_text='Selecione o nome do proprietário do local. Se não houver, insira um proprietário como Pessoa no sistema.', 
        blank=True,
        null=True,
        verbose_name='Pessoa física proprietária do local', 
        )

    proprietario_pj = models.ForeignKey(
        'instituicoes.Instituicao',
        help_text='selecione uma instituição proprietária da UR. Se não houver, insira a instituição no sistema.', 
        on_delete=models.SET_NULL, 
        blank=True,
        null=True,
        verbose_name='Pessoa jurídica proprietária do local', 
        )

    municipio = models.ForeignKey(
        Municipio,
        help_text='Selecione o municipio sede desta UR.', 
        on_delete=models.SET_NULL,  
        verbose_name='Município', 
        blank=True,
        null=True,
        )

    latitude = models.CharField(
        'Latitude',
        max_length=15,
        help_text='Insira a latitude em graus decimais com sinais. Exemplo: -28.123456', 
        default='-00.000000',
        blank=True,
        null=False,
        )

    longitude = models.CharField(
        'Longitude',
        max_length=15,
        help_text='Insira a longitude em graus decimais com sinais. Exemplo: -50.123456', 
        default='-00.000000', 
        blank=True,
        null=False,
        )

    projetos_vinculados = models.ManyToManyField(
        'projectos.Projeto', 
        verbose_name = 'Projeto(s) vinculado(s) ao local', 
        help_text = 'Insira um ou mais projetos aos quais este local está vinculado, se houver',
        blank=True, 
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    arquivos = models.FileField(
        upload_to='locais/unidades_de_referencia', 
        blank=True, 
        null=True,
        )

    def __str__(self):
        return 'URE' + str(self.id).zfill(3) + '-' + self.nome
    
    def get_absolute_url(self):
        """Traz a URL de perfil da unidade de referência."""
        return reverse('ur-detalhe', args=[str(self.id)])

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Unidade de de referência'
        verbose_name_plural = '05 - Unidades de referência'