
from datetime import date, datetime
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models
from django.contrib.gis.db import models
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

    def get_item_id(self): 
        return 'MBH' + str(self.id).zfill(3) + '-' + str(self.nome)[0:30] + '...'
    get_item_id.short_description = 'ID Codificada'

    def __str__(self): 
        return 'MBH' + str(self.id).zfill(3) + '-' + str(self.nome)[0:30] + '...'

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Microbracia'
        verbose_name_plural = 'Microbacias'



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

    def get_item_id(self): 
        return 'MUN' + str(self.id).zfill(3) + '-' + str(self.nome)[0:30] + '...'
    get_item_id.short_description = 'ID Codificada'

    def __str__(self):
        return 'MUN' + str(self.id).zfill(3) + '-' + str(self.nome)[0:30] + '...'

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'


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
    proprietario_pf_de_ur = models.ForeignKey(
        'pessoas.Pessoa',   
        on_delete=models.SET_NULL, 
        help_text='Selecione o nome do proprietário do local se for Pessoa Física.', 
        blank=True,
        null=True,
        verbose_name='Pessoa física proprietária do local', 
        )
    proprietario_pj_de_ur = models.ForeignKey(
        'instituicoes.Instituicao',
        help_text='Selecione uma instituição proprietária da UR, se for Pessoa Jurídica.', 
        on_delete=models.SET_NULL, 
        blank=True,
        null=True,
        verbose_name='Pessoa jurídica proprietária do local', 
        )
    municipio_da_ur = models.ForeignKey(
        Municipio,
        help_text='Selecione o municipio onde se localiza a UR.', 
        on_delete=models.SET_NULL,  
        verbose_name='Município da UR', 
        blank=True,
        null=True,
        )
    localizacao = models.PointField(
        'Local da atividade', 
        help_text='Encontre o local da sede da UR no mapa e depois insira um marcador sobre ela.', 
        blank=True, 
        null=True, 
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to='locais/unidades_de_referencia', 
        blank=True, 
        null=True,
        )

    def get_item_id(self):
        return 'URE' + str(self.id).zfill(3) + '-' + str(self.nome)[0:30] + '...'
    get_item_id.short_description = 'ID Codificada'

    def __str__(self):
        return 'URE' + str(self.id).zfill(3) + '-' + str(self.nome)[0:30] + '...'
    
    # def get_absolute_url(self):
    #     """Traz a URL de perfil da unidade de referência."""
    #     return reverse('ur-detalhe', args=[str(self.id)])

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Unidade de referência'
        verbose_name_plural = 'Unidades de referência'