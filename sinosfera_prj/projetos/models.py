from datetime import date, datetime
from django.urls import reverse
from django.conf import settings
from django.db import models
from email.policy import default
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, User


#########################################
### TABELAS DE HIERARQUIA DE EXECUÇÃO ###
#########################################

#=========================#
#== PROJETOS MUNICIPAIS ==#
#=========================#

class Projeto(models.Model):
    """Tabela de inserção dos dados relativos aos projetos municipais, em sua grande maioria. Outros projetos podem ser inseridos, mas a tabela foi construída com base nas necessidades de projetos municipais vinculados ao VerdeSinos.""",
    programa_vinculado_ao_projeto = models.ForeignKey(
        'programas.Programa',
        on_delete=models.SET_NULL,
        related_name='projetos_vinculados_ao_programa',
        help_text='Selecione o Programa de mobilização social a que este projeto se vincula.',
        blank=True,
        null=True,
        verbose_name='Programa de mobilização a que este projeto se vincula',
    )
    nome = models.CharField(
        'Nome ou título do projeto', 
        help_text='Defina um nome ou título curto ao projeto.', 
        max_length=120,
        blank=True,
        null=True,
    )
    objetivo_geral_do_projeto = models.TextField(
        'Objetivo geral do projeto', 
        help_text='Descreva o objetivo geral do projeto, ou o impacto que este deseja causar na sociedade e no meio ambiente.', 
        max_length=600,
        blank=True,
        null=True,
    )
    BOOL_CHOICES = ((True, 'Ativo'), (False, 'Encerrado'))
    encerrado = models.BooleanField(
        'Situação do Projeto',
        help_text='Selecione à situação atual deste projeto.', 
        choices=BOOL_CHOICES, 
        blank=True, 
        null=False,
        default=True,
    )
    resumo_descritivo_do_projeto = models.TextField(
        'Resumo descritivo do Projeto',
        help_text='Descreva de modo geral o que é, quem está envolvido, onde se dará a execução, quando deverá ocorrer a execução, como e porque o Projeto será executado.',
        blank=True,
        null=True,
    )
    fundos_de_execucao_do_projeto = models.TextField(
        'Descrição geral das fontes de recursos do Projeto',
        help_text='Descreva suscintamente de onde deverão vir ou vieram os recursos para este Projeto.',
        blank=True,
        null=True,
    )
    fundos_estimados_do_verde_sinos = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Especifique o total de fundos do VerdeSinos que este Projeto vai acessar ou acessou.',
        verbose_name='Total de fundos do VerdeSinos',
        blank=True,
        default=0,
    )
    fundos_estimados_de_contra_partida = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Especifique o total de contra-partida que este projeto vai acessar ou acessou.',
        verbose_name='Total de fundos de contra-partida',
        blank=True,
        default=0,
    )
    valor_total_do_projeto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        verbose_name='Valor total do Projeto',
        blank=True,
        default=0,
    )
    #== Ancoragens do Projeto ==#
    municipio_ancora_do_projeto = models.ForeignKey(
        'locais.Municipio',
        on_delete=models.SET_NULL,
        verbose_name='Município sede ou âncora do Projeto',
        help_text='Selecione o município cosiderado a sede ou âncora deste projeto.', 
        blank=True,
        null=True, 
    )
    urs_vinculadas_ao_projeto = models.ManyToManyField(
        'locais.Unidade_de_referencia',
        related_name='projetos_vinculados_a_ur',
        verbose_name='UR(s) vinculada(s) ao Projeto',
        help_text='Selecione uma ou mais URs que estão diretamente relacionadas ao projeto.',
        blank=True,
    )
    instituicao_ancora_do_projeto = models.ForeignKey(
        'instituicoes.Instituicao',
        on_delete=models.SET_NULL,
        verbose_name='Instituição âncora do Projeto',
        help_text='Selecione a Instituição considerada a proponente principal ou a âncora do Projeto',
        blank=True,
        null=True,
    )
    pessoa_ancora_do_projeto = models.ForeignKey(
        'pessoas.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Especifique a pessoa âncora, ou coordenadora deste projeto.', 
        blank=True,
        null=True,
        verbose_name='Coordenador(a) geral de Projeto', 
    )
    inicio = models.DateField(
        'Data de início do Projeto',
        default=date.today, 
        help_text='Especifique uma data estimada ou definida de início deste Projeto.', 
        blank=True,
        null=False, 
    )
    fim = models.DateField(
        'Data de fim do Projeto',
        default=date.today, 
        help_text='Especifique uma data estimada ou definida para a conclusão deste Projeto.', 
        blank=True,
        null=False, 
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to='projetos', 
        blank=True, 
        null=True,
    )
    
    # def save_model(self, request, obj, form, change):
    #     """Grava usuário logado que gravou o item"""
    #     obj.inserido_por = request.user
    #     super().save_model(request, obj, form, change)

    def save(self, *args, **kwargs):
        """Grava o Projeto com o valor total dele somando os fundos do VerdeSinos com a contra-partida."""
        self.valor_total_do_projeto = self.fundos_estimados_do_verde_sinos + self.fundos_estimados_de_contra_partida
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     """Traz a URL de perfil do Projeto."""
    #     return reverse('projeto-detalhe', args=[str(self.id)])

    def get_item_id(self):
        return 'PRJ' + str(self.id).zfill(4) + '-' + str(self.nome)[0:30] + '...'
    get_item_id.short_description = 'ID Codificada'

    def __str__(self):
        return 'PRJ' + str(self.id).zfill(4) + '-' + str(self.nome)[0:30] + '...'

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

#==================================================#
#== OBJETIVOS ESPECÍFICOS / SUB-PROJETOS / METAS ==#
#==================================================#

class Objetivo_especifico_de_projeto(models.Model):
    """Tabela para inserção de dados sobre os objetivos específicos que podem ser tratados como sub-projetos ou mais precisamente metas do projeto. São partes manejáveis do projeto que precisam ser conduzidas com determinação métrica e acompanhadas para o sucesso do Projeto."""
    projeto_vinculado_ao_objetivo_especifico = models.ForeignKey(
        Projeto,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Selecione o Projeto a que este objetivo específico, sub-projeto ou meta se vincula.',
        verbose_name='Projeto vinculado',
        )
    parent_subprojects = models.ManyToManyField(
        'self', 
        blank=True, 
        symmetrical=False, 
        related_name='child_subprojects',
        verbose_name='Subprojeto vinculado',
        )

    categoria_de_objetivo_especifico = models.ForeignKey(
        'categorias.Categoria_de_objetivo_especifico',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Selecione a categoria mais adequada para este objetivo específico.',
        verbose_name='Categoria',
        )
    nome = models.CharField(
        'Nome ou título do objetivo específico', 
        help_text='Defina um nome ou título curto para este objetivo específico.', 
        max_length=120,
        blank=True,
        null=True,
        )
    descricao_do_objetivo_especifico = models.TextField(
        'Descrição do objetivo específico', 
        help_text='Descreva o que este objetivo específico pretende alcançar.', 
        max_length=300,
        blank=True,
        null=True,
        )
    coordenador = models.ForeignKey(
        'pessoas.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Especifique a pessoa âncora ou coordenadora deste objetivo específico.', 
        blank=True, 
        null=True, 
        verbose_name='Coordenador(a) de Objetivo específico', 
        )
    indicadores = models.TextField(
        'Indicadores', 
        max_length=300, 
        help_text='Especifique aqui o(s) indicador(es) que evidenciarão o alcance deste objetivo específico.', 
        blank=True, 
        null=True, 
        )
    verificacao = models.TextField(
        'Métodos de verificação', 
        max_length=300, 
        help_text='Especifique aqui como serão verificados os indicadores de alcance dos objetivos, isto é que instromentos, metodologia, processos.', 
        blank=True, 
        null=True, 
    )
    percentual_de_alcance_atingido = models.IntegerField(
        'Percentual de alcance atingido',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Insira um valor de 0 a 100 correspondente ao percentual de alcance deste objetivo até o momento.',
        blank=True, 
        null=False,
        default=0,
        )
    inicio = models.DateField(
        'Data de início do Objetivo específico',
        default=date.today, 
        help_text='Especifique uma data de início para o objetivo específico.', 
        blank=True,
        null=False, 
        )
    fim = models.DateField(
        'Data de fim do objetivo específico',
        default=date.today, 
        help_text='Defina uma data para a conclusão do objetivo específico.', 
        blank=True,
        null=False, 
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to='projetos/objetivos_especificos', 
        blank=True, 
        null=True,
        )

    # def save_model(self, request, obj, form, change):
    #     '''Grava usuário logado que gravou o item'''
    #     obj.inserido_por = request.user
    #     super().save_model(request, obj, form, change)

    def get_item_id(self):
        return 'OBJ' + str(self.id).zfill(4) + '-' + str(self.nome)[0:30] + '...'
    get_item_id.short_description = 'ID Codificada'

    def __str__(self):
        return 'OBJ' + str(self.id).zfill(4) + '-' + str(self.nome)[0:30] + '...'

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Objetivo específico'
        verbose_name_plural = 'Objetivos específicos'

#============#
#== ETAPAS ==#
#============#

class Etapa(models.Model):    
    """Tabela de inserção de dados das pequenas etapas necessárias para alcance os objetivos específicos, sub-projetos ou metas especificadas para o Projeto."""
    objetivo_especifico_vinculado_a_etapa = models.ForeignKey(
        Objetivo_especifico_de_projeto, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o objetivo específico a que esta etapa se vincula.', 
        blank=True, 
        null=True, 
        verbose_name='Objetivo específico vinculado à etapa', 
        )
    nome = models.CharField(
        'Nome ou título da etapa', 
        help_text='Defina um nome ou título para a etapa de um objetivo específico.',  
        max_length=120,
        blank=True,
        null=True,
        )
    descricao = models.TextField(
        'Descrição da etapa', 
        max_length=600, 
        help_text='Descreva suscintamente a etapa com algumas atividades que serão necessárias para concluí-la.', 
        blank=True,
        null=True,
        )
    concluida = models.BooleanField(
        'Concluida', 
        blank=True, 
        null=False,
        default=False,
        help_text='Marque a caixa de seleção se a etapa já está concluída',
        )
    coordenador = models.ForeignKey(
        'pessoas.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Selecione a pessoa âncora, coordenadora, responsável pela etapa.', 
        blank=True, 
        null=True, 
        verbose_name='Coordenador(a) de etapa', 
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def get_item_id(self):
        return 'ETA' + str(self.id).zfill(5) + '-' + str(self.nome)[0:30] + '...'
    get_item_id.short_description = 'ID Codificada'

    def __str__(self):
        return 'ETA' + str(self.id).zfill(5) + '-' + str(self.nome)[0:30] + '...'


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'

#================#
#== ATIVIDADES ==#
#================#

class Atividade(models.Model):    
    """Model to input details about project activities."""
    # == VÍNCULOS DA ATIVIDADE == #
    projeto_vinculado = models.ForeignKey(
        Projeto, 
        on_delete=models.SET_NULL, 
        help_text='Insira o projeto ao qual essa atividade se vincula',
        blank=True, 
        null=True, 
        verbose_name='Projeto vinculado', 
    )
    objetivo_especifico_vinculado = models.ForeignKey(
        Objetivo_especifico_de_projeto, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o objetivo específico a que esta atividade se vincula, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Objetivo específico vinculado', 
        )
    etapa_vinculada = models.ForeignKey(
        Etapa, 
        on_delete=models.SET_NULL, 
        help_text='Insira a etapa que esta atividade está diretamente vinculada, se houver',
        blank=True,
        null=True, 
        verbose_name='Etapa vinculada', 
    )
    # == Dados básicos da atividade == #
    nome = models.CharField(
        'Nome ou título da atividade', 
        help_text='Defina um título ou nome curto para a atividade36+.',  
        max_length=120,
        blank=True,
        null=True,
        )
    descricao = models.TextField(
        'Descrição',  
        help_text='Descreva a atividade com o maior número possível de detalhes relevantes.', 
        blank=True,
        null=True,
        )
    inicio = models.DateTimeField(
        'Início',
        default=None, 
        help_text='Especifique a data e hora de início da atividade.', 
        blank=True,
        null=True, 
        )
    fim = models.DateTimeField(
        'Fim',
        default=None, 
        help_text='Especifique a data e hora de finalização da atividade.', 
        blank=True,
        null=True,  
        )
    concluida = models.BooleanField(
        'Concluída',
        help_text='Marque a caixa de seleção se esta atividade já está concluída ou já foi executada.', 
        blank=True, 
        null=False,
        default=False,
        )
    coordenador = models.ForeignKey(
        'pessoas.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Especifique a pessoa âncora ou coordenadora desta atividade.', 
        blank=True, 
        null=True, 
        verbose_name='Coordenador(a) de Atividade', 
        )
    base_curricular_vinculada = models.TextField(
        'Base curricular', 
        max_length=300, 
        help_text='Se for atividade docente, descreva brevemente as relações com a base curricular vigente.', 
        blank=True,
        null=True,
        )    
    categoria_de_atividade = models.ForeignKey(
        'categorias.Categoria_de_atividade',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Selecione a categoria mais adequada para esta atividade.',
        verbose_name='Categoria',
        )
    sub_categoria_de_atividade = models.ForeignKey(
        'categorias.Sub_categoria_de_atividade',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text='Selecione a subcategoria da atividade.',
        verbose_name='Subcategoria',
    )
    # == Localização da atividade == #
    municipio = models.ForeignKey(
        'locais.Municipio',  
        on_delete=models.SET_NULL, 
        verbose_name='Município sede da atividade', 
        blank=True,
        null=True,
        )
    ur_vinculada = models.ForeignKey(
        'locais.Unidade_de_referencia', 
        on_delete=models.SET_NULL, 
        help_text='Selecione o local de referência onde esta atividade está vinculada, se houver',
        blank=True, 
        null=True, 
        verbose_name='Unidade de referência vinculada',
    )
    localizacao = models.PointField(
        'Local da atividade', 
        help_text='Encontre o local da atividade no mapa e depois insira um marcador sobre ele.', 
        blank=True, 
        null=True, 
    )
    resultados = models.TextField(
        'Resultados', 
        max_length=600, 
        help_text='Registre aqui o que se alcançou com a atividade depois de concluída.', 
        blank=True,
        null=True,
        )
    publico_envolvido = models.PositiveIntegerField(
        default=0, 
        editable=False,
        verbose_name='Público diretamente envolvido',
        blank=True,
        null=True,
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to='projetos/atividades', 
        blank=True, 
        null=True,
        )

    def get_publico_total(self):
        # Calculate and return the total quantity of public attended for this activity
        return Publico.objects.filter(atividade=self).aggregate(publico_total=models.Sum('quantidade'))['publico_total']
    get_publico_total.short_description ='Público total'

    def get_item_id(self):
        return 'ATV' + str(self.id).zfill(5) + '-' + str(self.nome)[0:30] + '...'
    get_item_id.short_description = 'ID Codificada'

    def __str__(self):
        return 'ATV' + str(self.id).zfill(5) + '-' + str(self.nome)[0:30] + '...'

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'


class Publico(models.Model):
    """Tabela de inserção de dados do público envolvido."""
    atividade = models.ForeignKey(
        Atividade,
        verbose_name='Atividade vinculada.',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text='Selecione a atividade vinculada ao público envolvido.',
    )
    categoria=models.ForeignKey(
        'categorias.Categoria_de_publico',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text='Selecione o tipo de público envolvido.',
        verbose_name='Categoria de público',
    )
    detalhamento = models.CharField(
        max_length=250,
        help_text='Inclua uma breve descrição do público envolvido.',
        blank=True,
        null=True,
        verbose_name='Detalhamento',
        )
    quantidade = models.PositiveIntegerField(
        help_text='Insira a quantidade de pessoas envolvidas da categoria selecionada.',
        verbose_name='QTD',
        default=0,
    )

    def save(self, *args, **kwargs):
        super(Publico, self).save(*args, **kwargs)
        # Calculate and update the total quantity of public attended for the related activity
        self.atividade.publico_envolvido = Publico.objects.filter(atividade=self.atividade).aggregate(publico_total=models.Sum('quantidade'))['publico_total'] or 0
        self.atividade.save()

    def __str__(self):
        return 'PUB' + str(self.id).zfill(3) + '-' + str(self.categoria)
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Público envolvido'
        verbose_name_plural = 'Públicos envolvidos'