from datetime import date, datetime
from django.db import models
from email.policy import default
from django.core.validators import RegexValidator

#==================#
#== INSTITUIÇÕES ==#
#==================#

class Instituicao(models.Model):
    """Tabela de inserção de dados das instituições parceiras, fornecedoras, proponentes, executoras e quaisquer instituição que fizer parte dos planos, programas e projetos neste sistema."""
    razao_social = models.CharField(
        'Razão Social', 
        default='', 
        help_text='Insira a razão social da instituição como consta no CNPJ ou o nome completo da mesma',
        max_length=150,
        blank=True,
        null=True,
        )
    nome_fantasia = models.CharField(
        'Nome fantasia', 
        default='', 
        help_text='Insira a sigla ou nome fantasia da instituição como consta no CNPJ ou o nome como é conhecida', 
        max_length=60,
        blank=True,
        null=True,
        )
    sem_cnpj = models.BooleanField(
        'Instituição sem CNPJ', 
        help_text='Marque a caixa de seleção se a Instituição não possui CNPJ.',
        blank=True, 
        null=False,
        default=False,
        )
    cnpj = models.CharField(
        CNPJNumberRegex = RegexValidator(regex = r"^\+?1?\d{14}$")
        'CNPJ',
        validators = [CNPJNumberRegex], 
        help_text='Insira somente os 14 dígitos do CNPJ.',  
        max_length=18,
        blank=True,
        null=True,
        unique=True,
        )
    #== ENDEREÇO DA INSTITUIÇÃO ==#
    # TODO: O endereço deverá ser preenchido de forma georeferenciada fazendo-se uso de API específica de mapas ou de geocodificação.
    # municipio = models.ForeignKey(
    #     'locais.Municipio', 
    #     on_delete=models.SET_NULL, 
    #     verbose_name = 'Município sede da instituição', 
    #     blank=True, 
    #     null=True, 
    #     )
    # latitude = models.CharField(
    #     'Latitude',
    #     max_length=15,
    #     help_text='Insira a latitude em graus decimais com sinais. Exemplo: -28.123456', 
    #     default='-00.000000',
    #     blank=True,
    #     null=True,
    #     )
    # longitude = models.CharField(
    #     'Longitude',
    #     max_length=15,
    #     help_text='Insira a longitude em graus decimais com sinais. Exemplo: -50.123456', 
    #     default='-00.000000', 
    #     blank=True,
    #     null=True,
    #     )
    #== DADOS DE CONTATO COM A INSTITUIÇÃO ==#
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    telefone = models.CharField(
        'Telefone comercial', 
        validators = [phoneNumberRegex], 
        max_length = 16,  
        help_text='Insira somente dígitos e Inclua o código de área',  
        blank=True,
        null=True, 
        )
    email = models.EmailField(
        'E-mail', 
        default=' ',  
        blank=True,
        null=True,
        )
    url = models.URLField(
        'URL', 
        default='',  
        blank=True,
        null=True,
        )
    responsavel_pela_instituicao = models.ForeignKey(
        'pessoas.Pessoa', 
        on_delete=models.SET_NULL,
        verbose_name='Pessoa responsável, representante ou âncora da instituição', 
        blank=True, 
        null=True, 
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to='locais/instituicoes',
        blank=True, 
        null=True,
        )

    def __str__(self): 
        return 'INS' + str(self.id).zfill(3) + '-' + self.nome_fantasia

    class Meta:
        ordering = ('nome_fantasia',)
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'
