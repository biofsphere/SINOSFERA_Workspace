from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User

#======================================#
#== TABELA DE SOLICITAÇÕES DE FUNDOS ==#
#======================================#

class Solicitacao_de_fundos(models.Model):
    municipio_solicitante = models.ForeignKey(
        'locais.Municipio',
        on_delete=models.NULL,
        help_text='Selecione o município para onde irão os fundos',
        blank=True,
        null=True,
        verbose_name='Município recebedor',
        )
    responsavel_pelo_preenchimento = models.ForeignKey(
        'pessoas.Pessoa',
        on_delete=models.NULL,
        help_text='Selecione a pessoa responsável pelo preenchimento desta solicitação.',
        blank=True,
        null=True,
        verbose_name='Responsável pelo preenchimento desta solicitação',
        )
    # == VÍNCULOS DA ATIVIDADE == #
    ur_relacionada = models.OneToOneField(
        'locais.Unidade_de_referencia',
        on_delete=models.NULL,
        help_text='Selecione a UR relacionada a esta solicitação, se houver.',
        blank=True,
        null=True,
        verbose_name='UR recebedora',
        )    
    projeto_vinculado = models.OneToOneField(
        'projetos.Projeto', 
        on_delete=models.NULL, 
        help_text='Insira o projeto ao qual essa atividade se vincula',
        blank=True, 
        null=True, 
        verbose_name='Projeto recebedor', 
    )
    objetivo_especifico_vinculado = models.ForeignKey(
        'projetos.Objetivo_especifico_de_projeto', 
        on_delete=models.SET_NULL, 
        help_text='Selecione o objetivo específico a que esta atividade se vincula, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Objetivo específico vinculado', 
        )
    meta_vinculada = models.ForeignKey(
        'projetos.Meta_de_objetivo_especifico_de_projeto', 
        on_delete=models.SET_NULL, 
        help_text='Selecione a meta a que esta solicitação se vincula, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Meta vinculada', 
        )
    etapa_vinculada = models.ForeignKey(
        Etapa, 
        on_delete=models.SET_NULL, 
        help_text='Insira a etapa que esta atividade está diretamente vinculada, se houver',
        blank=True,
        null=True, 
        verbose_name='Etapa vinculada', 
    )
    atividade_vinculada = models.ForeignKey(
        'projetos.Atividade',
        on_delete=models.CASCADE,
        help_text='Selecione a(s) atividade(s) relacionada(s) a esta solicitação.',
        blank=True,
        null=True,
    
    def __str__(self):
        return 'SOL' + str(self.id).zfill(6)