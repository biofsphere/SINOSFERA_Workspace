from datetime import date, datetime
from django.urls import reverse
from django.db import models
from email.policy import default
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, User

###############################
### TABELAS DE PLANEJAMENTO ###
###############################

#======================#
#== PLANO PLURIANUAL ==#
#======================#

class Plano(models.Model):
    nome = models.CharField(
        'Nome ou título', 
        help_text='Esse é o plano maior. Pode ser um plano municipal ou regional. Defina um nome para o plano plurianual.', 
        max_length=120,
        blank=True,
        null=True,
        )

    obj_geral = models.TextField(
        'Objetivo geral', 
        help_text='Descreva de modo geral o que o plano plurianual pretende alcançar.', 
        max_length=600,
        blank=True,
        null=True,
        )

    municipios = models.ManyToManyField(
        'places.Municipio', 
        verbose_name='Municípios', 
        blank=True, 
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
