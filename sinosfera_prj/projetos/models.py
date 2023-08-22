from datetime import date, datetime
from django.urls import reverse
from django.conf import settings
from django.db import models
from email.policy import default
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, User


############################################
### TABELAS DE INICIATIVAS PARA EXECUÇÃO ###
############################################


#=========================#
#== PROJETOS MUNICIPAIS ==#
#=========================#


class Projeto(models.Model):
    programa_vinculado = models.ForeignKey(
        'programas.Programa',
        on_delete=models.SET_NULL,
        help_text='Selecione o Programa de mobilização social a que este projeto se vincula.',
        blank=True,
        null=True,
        verbose_name='Programa de mobilização vinculado',
    )
    nome = models.CharField(
        'Nome ou título do projeto', 
        help_text='Defina um nome ou título curto ao projeto.', 
        max_length=120,
        blank=True,
        null=True,
        )
    objetivo_geral = models.TextField(
        'Objetivo geral', 
        help_text='Descreva o objetivo geral do projeto, ou o impacto que este deseja causar na sociedade e no meio ambiente.', 
        max_length=600,
        blank=True,
        null=True,
        )
    BOOL_CHOICES = ((True, 'Ativo'), (False, 'Encerrado'))
    encerrado = models.BooleanField(
        'Situação',
        help_text='Selecione à situação atual deste projeto.', 
        choices=BOOL_CHOICES, 
        blank=True, 
        null=False,
        default=True,
        )
    municipio = models.ForeignKey(
        'locais.Municipio',
        help_text='Selecione o município sede deste projeto.',  
        on_delete=models.SET_NULL,  
        verbose_name='Município sede do projeto', 
        blank=True,
        null=True,
        )
    coordenador = models.ForeignKey(
        'pessoas.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Selecione a pessoa âncora ou coordenadora geral deste projeto.', 
        blank=True, 
        null=True, 
        verbose_name='Coordenador(a) geral', 
        )
    instituicao_ancora = models.ManyToManyField(
        'places.Instituicao', 
        help_text='Selecione as instituições parceiras nesse projeto',
        blank=True,
        verbose_name='Instituições parceiras nesse projeto', 
        )
    inicio = models.DateField(
        'Início',
        default=date.today, 
        help_text='Especifique uma data de início para o projeto.', 
        blank=True,
        null=False, 
        )
    final = models.DateField(
        'Fim',
        default=date.today, 
        help_text='Defina uma data para a conclusão do projeto.', 
        blank=True,
        null=False, 
        )
    projetos_vinculados = models.ManyToManyField(
        'self', 
        help_text='Insira um ou mais projetos que estão diretamente vinculados a este projeto',
        blank=True,
        verbose_name='Projetos vinculados', 
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to=r'projects_media\prj_media', 
        blank=True, 
        null=True,
        )
    
    # inserido_por = models.ForeignKey(
    #     User,
    #     on_delete=models.SET_NULL, 
    #     help_text='Esse campo se preenche automaticamente com o nome do usuário que grava a inserção de dados',
    #     blank=True, 
    #     null=True,
    #     )

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def get_absolute_url(self):
        """Traz a URL de perfil do Projeto."""
        return reverse('projeto-detalhe', args=[str(self.id)])

    def __str__(self):
        return 'PRJ' + str(self.id).zfill(3) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Projeto'
        verbose_name_plural = '10 - Projetos'


#==================#
#== SUB-PROJETOS ==#
#==================#


class Sub_projeto(models.Model):
    CATEGORIAS_DE_SUB_PROJETOS = [
        ('Projeto ambiental', (
            ('03', '03 - Projeto de restauração ecológica'),
            ('04', '04 - Plano de manejo de fauna'),
            ('05', '05 - Plano de manejo de flora'),
            ('06', '06 - Plano de manejo de solo'),
            ('07', '07 - Plano de manejo de água'),
            ('08', '08 - Plano de manejo de UR ou UC'),
            ('09', '09 - Plano de monitoramento ambiental'),
            ('10', '10 - Outro projeto ambiental'),
        )),
        ('Projeto social', (
            ('11', '11 - Plano de comunicação'),
            ('12', '12 - Projeto de avaliação'),
            ('13', '13 - Plano de mobilização social'),
            ('14', '14 - Outro projeto social'),
        )),
        ('Projeto acadêmico', ( 
            ('15', '15 - Congresso'),
            ('16', '16 - Seminário'),
            ('17', '17 - Fórum'),
            ('18', '18 - Simpósio'),
            ('19', '19 - Colóquio'),
            ('20', '20 - Painel'),
            ('21', '21 - Reunião acadêmica'),
            ('22', '22 - Curso ou programa educacional'),
            ('23', '23 - Projeto de pesquisa ou estudo'),
            ('24', '24 - Outro projeto acadêmico'),
        )),
        ('Evento não-acadêmico', (
            ('25', '25 - Festa ou celebração'),
            ('26', '26 - Feira ou mercado'),
            ('27', '27 - Exibição ou exposição'),
            ('28', '28 - Campanha ou mobilização'),
            ('29', '29 - Curso ou treinamento'),
            ('30', '30 - Outro evento não-acadêmico'),
        )),
        ('Projeto de desenvolvimento', (
            ('31', '31 - Construção ou reforma,'),
            ('32', '32 - Instalação'),
            ('33', '33 - Desenvolvimento de TI'),
            ('34', '34 - Outro projeto de desenvolvimento'),
        )),
        ('Qualquer outro tipo de sub-projeto'),
    ]
    projeto_vinculado = models.ForeignKey(
        Pro
    nome = models.CharField(
        'Nome ou título do sub-projeto', 
        help_text='Defina o nome ou título do projeto.', 
        max_length=120,
        blank=True,
        null=True,
        )
    objetivo_geral = models.TextField(
        'Objetivo geral', 
        help_text='Descreva o objetivo geral do projeto, ou o impacto que este deseja causar na sociedade e no meio ambiente.', 
        max_length=600,
        blank=True,
        null=True,
        )
    BOOL_CHOICES = ((True, 'Ativo'), (False, 'Encerrado'))
    encerrado = models.BooleanField(
        'Situação',
        help_text='Selecione à situação atual do projeto.', 
        choices=BOOL_CHOICES, 
        blank=True, 
        null=False,
        default=True,
        )
    municipio = models.ForeignKey(
        'locais.Municipio',
        help_text='Selecione o município sede do projeto.',  
        on_delete=models.SET_NULL,  
        verbose_name='Município sede do projeto', 
        blank=True,
        null=True,
        )
    coordenador = models.ForeignKey(
        'pessoas.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Especifique a pessoa coordenadora do projeto.', 
        blank=True, 
        null=True, 
        verbose_name='Coordenador geral', 
        )
    acoes_vinculadas = models.ManyToManyField(
        'plans.Acao', 
        help_text='Especifique uma ou mais ações prioritárias do programa de ações do plano plurianual ao qual o projeto se vincula.', 
        blank=True, 
        verbose_name='Ações prioritárias vinculadas', 
        )
    instituicoes_vinculadas = models.ManyToManyField(
        'places.Instituicao', 
        help_text='Selecione as instituições parceiras nesse projeto',
        blank=True,
        verbose_name='Instituições parceiras nesse projeto', 
        )
    inicio = models.DateField(
        'Início',
        default=date.today, 
        help_text='Especifique uma data de início para o projeto.', 
        blank=True,
        null=False, 
        )
    final = models.DateField(
        'Fim',
        default=date.today, 
        help_text='Defina uma data para a conclusão do projeto.', 
        blank=True,
        null=False, 
        )
    projetos_vinculados = models.ManyToManyField(
        'self', 
        help_text='Insira um ou mais projetos que estão diretamente vinculados a este projeto',
        blank=True,
        verbose_name='Projetos vinculados', 
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to=r'projects_media\prj_media', 
        blank=True, 
        null=True,
        )
    
    # inserido_por = models.ForeignKey(
    #     User,
    #     on_delete=models.SET_NULL, 
    #     help_text='Esse campo se preenche automaticamente com o nome do usuário que grava a inserção de dados',
    #     blank=True, 
    #     null=True,
    #     )

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def get_absolute_url(self):
        """Traz a URL de perfil do Projeto."""
        return reverse('projeto-detalhe', args=[str(self.id)])

    def __str__(self):
        return 'PRJ' + str(self.id).zfill(3) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Projeto'
        verbose_name_plural = '10 - Projetos'


#===========================#
#== OBJETIVOS ESPECÍFICOS ==#
#===========================#

class Objetivo_especifico_de_projeto(models.Model):    
    nome = models.CharField(
        'Nome ou título', 
        help_text='Defina um título ou nome curto para o objetivo específico do projeto.', 
        max_length=120,
        blank=True,
        null=True,
        )
    descricao = models.TextField(
        'Descrição', 
        help_text='Descreva o objetivo de forma específica, observável, que seja alcançável e relevante.', 
        max_length=600,
        blank=True,
        null=True,
        )
    alcancado = models.BooleanField(
        'Alcançado',
        help_text='Marque a caixa de seleção se este objetivo já foi plenamente alcançado.',
        blank=True, 
        null=False,
        default=False,
        )

    proj_vinculado = models.ForeignKey(
        Projeto, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o projeto ao qual o objetivo específico está vinculado, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Projeto vinculado', 
        )

    coordenador = models.ForeignKey(
        'people.Pessoa',  
        on_delete=models.SET_NULL, 
        help_text='Selecione a pessoa âncora ou coordenadora do objetivo específico, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Coordenador geral do objetivo específico', 
        )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    arquivos = models.FileField(
        upload_to=r'projects_media\obj_media', 
        blank=True, 
        null=True,
        )

    # def get_absolute_url(self):
    #     """Traz a URL de perfil do Objetivo Específico."""
    #     return reverse('obj_esp-detalhe', args=[str(self.id)])

    def __str__(self):
        return 'OBJ' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Objetivo específico'
        verbose_name_plural = '11 - Objetivos específicos'



#===========#
#== METAS ==#
#===========#

class Meta_de_objetivo_especifico_de_projeto(models.Model):
    # CATEGORIAS_DE_METAS = [
    #     ('01', '01 - Ambiental'),
    #     ('02', '02 - Social'),
    #     ('03', '03 - Econômica'),
    #     ('04', '04 - Legal'),
    #     ('05', '05 - Mista'),
    #     ('06', '06 - Outra'),
    # ]
    
    nome = models.CharField(
        'Nome ou título da meta', 
        help_text='Defina um título ou nome para a meta que deseja alcançar.', 
        max_length=120,
        blank=True,
        null=True,
        )

    descricao = models.TextField(
        'Descrição', 
        help_text='Descreva a meta de forma específica, mensurável, alcançável dentro de um prazo hábil.', 
        max_length=600,
        blank=True,
        null=True,
        )

    indicadores = models.TextField(
        'Indicadores', 
        max_length=300, 
        help_text="Considere a categoria da meta e especifique aqui o(s) indicador(es) quantitativo(s).", 
        blank=True, 
        null=True, 
    )

    verificacao = models.TextField(
        'Métodos de verificação', 
        max_length=300, 
        help_text="Considere os indicadores especificados anteriormente e especifique aqui as formas que estes serão verificados.", 
        blank=True, 
        null=True, 
    )

    # categoria = models.CharField(
    #     'Categoria de meta',
    #     choices = CATEGORIAS_DE_METAS,  
    #     help_text='Selecione a categoria que essa meta se enquadra melhor.', 
    #     max_length=100,
    #     blank=True, 
    #     null=True, 
    # )

    prazo = models.DateField(
        'Prazo',
        help_text='Data em que se espera que esta meta seja atingida.',
        blank=True, 
        null=True, 
    )

    #BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))

    alcancada = models.BooleanField(
        'Alcançada', 
        #choices=BOOL_CHOICES, 
        blank=True, 
        null=False,
        default=False,
        )

    categoria = models.OneToOneField(
        'categories.Categoria_met', 
        on_delete=models.SET_NULL, 
        #choices = CATEGORIAS_DE_METAS,
        blank=True, 
        null=True,
        verbose_name='Categoria de meta', 
    )

    obj_esp_vinculado = models.ForeignKey(
        Obj_esp, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o objetivo específico a que este meta se vincula.', 
        blank=True, 
        null=True, 
        verbose_name='Objetivo específico vinculado', 
        )

    proj_vinculado = models.ForeignKey(
        Projeto, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o projeto ao qual esta meta está vinculada.',
        blank=True, 
        null=True, 
        verbose_name='Projeto vinculado', 
    )

    coordenador = models.ForeignKey(
        'people.Pessoa',  
        on_delete=models.SET_NULL, 
        help_text='Selecione a pessoa âncora ou coordenadora desta meta, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Coordenador geral desta meta', 
        )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    arquivos = models.FileField(
        upload_to='projetos\metas', 
        blank=True, 
        null=True,
        )

    # def get_absolute_url(self):
    #     """Traz a URL de perfil da Meta de um objetivo específico."""
    #     return reverse('metaobj-detalhe', args=[str(self.id)])

    def __str__(self):
        return 'MET' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Meta'
        verbose_name_plural = '12 - Metas'



#============#
#== ETAPAS ==#
#============#

class Etapa(models.Model):    
    # CATEGORIAS_DE_ETAPAS = [
    #     ('Obras e serviços', (
    #         ('01', '01 - Manejo da flora'),
    #         ('02', '02 - Manejo da fauna'),
    #         ('03', '03 - Manejo do solo'),
    #         ('04', '04 - Manejo de água'),
    #         ('05', '05 - Instalação'),
    #         ('06', '06 - Construção'),
    #         ('07', '07 - Edificação'),
    #         ('08', '08 - Manutenção'),
    #         ('09', '10 - Outra obra ou serviço'),
    #     )),
    #     ('Outras categorias', (
    #         ('10', '10 - Etapa de evento acadêmico',),
    #         ('11', '11 - Etapa de evento não-acadêmico'),
    #         ('12', '12 - Outra etapa qualquer'),
    #     )), 
    #     ]
    
    nome = models.CharField(
        'Nome ou título', 
        help_text='Defina um título para a etapa.',  
        max_length=120,
        blank=True,
        null=True,
        )

    descricao = models.TextField(
        'Descrição', 
        max_length=600, 
        help_text='Descreva a etapa com algumas atividades que serão necessárias para cumpri-la.', 
        blank=True,
        null=True,
        )

    categoria = models.OneToOneField(
        'categories.Categoria_eta', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        verbose_name='Categoria de etapa', 
    )

    # categoria = models.CharField(
    #     'Categoria', 
    #     choices = CATEGORIAS_DE_ETAPAS, 
    #     help_text='Selecione uma das categorias de etapas disponíveis', 
    #     max_length=100,
    #     blank=True,
    #     null=True,
    #     )

    #BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))

    concluida = models.BooleanField(
        'Concluida', 
        #choices=BOOL_CHOICES, 
        blank=True, 
        null=False,
        default=False,
        )

    coordenador = models.ForeignKey(
        'people.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Selecione a pessoa âncora, coordenadora, responsável pela etapa.', 
        blank=True, 
        null=True, 
        verbose_name='Responsável pela etapa', 
        )

    meta_vinculada = models.ForeignKey(
        MetaObj, 
        on_delete=models.SET_NULL, 
        help_text='Selecione a meta a que esta etapa se vincula, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Meta vinculada', 
        )

    obj_esp_vinculado = models.ForeignKey(
        Obj_esp, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o objetivo específico a que esta etapa se vincula, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Objetivo específico vinculado', 
        )

    proj_vinculado = models.ForeignKey(
        Projeto, 
        on_delete=models.SET_NULL, 
        help_text='Insira o projeto ao qual essa etapa se vincula',
        blank=True, 
        null=True, 
        verbose_name='Projeto vinculado', 
    )

    local_vinculado = models.ForeignKey(
        'places.Local', 
        on_delete=models.SET_NULL, 
        help_text='Selecione o Local de Referência onde esta etapa está vinculada, se houver',
        blank=True, 
        null=True, 
        verbose_name='Local de referência vinculado',
    )
    
    municipio = models.ForeignKey(
        'places.Municipio',  
        on_delete=models.SET_NULL, 
        verbose_name='Município sede desta etapa', 
        blank=True,
        null=True,
        )

    inicio = models.DateField(
        'Início',
        default=None, 
        help_text='Especifique a data de início desta etapa.', 
        blank=True,
        null=True, 
        )
    
    final = models.DateField(
        'Fim',
        default=None, 
        help_text='Especifique a data de finalização desta etapa.', 
        blank=True,
        null=True,  
        )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    arquivos = models.FileField(
        upload_to=r'projects_media\eta_media', 
        blank=True, 
        null=True,
        )

    # def get_absolute_url(self):
    #     """Traz a URL de perfil da Etapa."""
    #     return reverse('etapa-detalhe', args=[str(self.id)])

    def __str__(self):
        return 'ETA' + str(self.id).zfill(5) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Etapa'
        verbose_name_plural = '13 - Etapas'

#================#
#== ATIVIDADES ==#
#================#

class Atividade(models.Model):    
    """Model to input details about project activities."""
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
        #choices=BOOL_CHOICES, 
        blank=True, 
        null=False,
        default=False,
        )
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
        Obj_esp, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o objetivo específico a que esta atividade se vincula, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Objetivo específico vinculado', 
        )
    meta_vinculada = models.ForeignKey(
        MetaObj, 
        on_delete=models.SET_NULL, 
        help_text='Selecione a meta a que esta atividade se vincula, se houver.', 
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
    base_curricular_vinculada = models.TextField(
        'Base curricular', 
        max_length=300, 
        help_text='Se for atividade docente, descreva brevemente as relações com a base curricular vigente.', 
        blank=True,
        null=True,
        )    
    # == Classificação da Atividade == #
    CATEGORIAS_DE_ATIVIDADES = [ 
        ('Docência da Educação Básica', (
            ('01', '01 - Artística, lúdica,'),
            ('02', '02 - Audiovisual, multimídia'),
            ('03', '03 - Demonstração, experiência'),
            ('04', '04 - Debate, diálogo'),
            ('05', '05 - Leitura, escrita'),
            ('06', '06 - Palestra, expositiva'),
            ('07', '07 - Trilha, visita, campo'),
            ('08', '08 - Oficina, mini-curso'),
            ('09', '09 - Avaliação, teste,'),
            ('10', '10 - Ativismo, mobilização'),
            ('11', '11 - Outra metodologia'),
        )),
        ('Atendimento sem docência', (
            ('12', '12 - Visita',),
            ('13', '13 - Assessoria'),
            ('14', '14 - Outro atendimento'),
        )),
        ('Capacitação técnica', (
            ('15', '15 - Curso de capacitação',),
            ('16', '16 - Oficina prática'),
            ('17', '17 - Palestra'),
            ('18', '18 - Outra capacitação'),
        )),
        ('Manutenção de recurso', (
            ('19', '19 - Limpeza',),
            ('20', '20 - Conserto'),
            ('21', '21 - Mudança'),
            ('22', '22 - Outra manutenção'),
        )),
        ('Confecção', (
            ('23', '23 - Jardinagem'),
            ('24', '24 - Material didático'),
            ('25', '25 - Peças de comunicação'),
            ('26', '26 - Artesanato'),
            ('27', '27 - Outra confecção'),
        )),
        ('Gestão ou administração', (
            ('28', '28 - Reunião interna'),
            ('29', '29 - Atividade individual'),
            ('30', '30 - Supervisão'),
            ('31', '31 - Logística'),
            ('32', '32 - Tramitação'),
            ('33', '33 - Comunicação'),
            ('34', '34 - Organização'),
            ('35', '35 - Outra atividade de gestão'),
        )),
        ('Outra categoria de atividade', (
            ('36', '36 - Outra categoria qualquer'),
        )),
        ]
    # categoria = models.CharField(
    #     'Categoria', 
    #     choices = CATEGORIAS_DE_ATIVIDADES, 
    #     help_text='Selecione uma das categorias de atividades ou tarefas disponíveis', 
    #     max_length=100,
    #     blank=True,
    #     null=True,
    #     )
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
    # onde = models.CharField(
    #     'Local da atividade', 
    #     help_text='Especifique o local ou ambiente onde se deu a atividade.',
    #     max_length=120, 
    #     blank=True, 
    #     null=True, 
    # )
    # resultados = models.TextField(
    #     'Resultados', 
    #     max_length=600, 
    #     help_text='Descreva o que se alcançou com a atividade após concluída.', 
    #     blank=True,
    #     null=True,
    #     )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    arquivos = models.FileField(
        upload_to='projetos/atividades', 
        blank=True, 
        null=True,
        )

    def __str__(self):
        return 'ATV' + str(self.id).zfill(5) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Atividade'
        verbose_name_plural = '14 - Atividades'
