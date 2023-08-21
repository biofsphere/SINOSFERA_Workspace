from datetime import date, datetime
from django.urls import reverse
from django.conf import settings
from django.db import models
from email.policy import default
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, User


###################################################
### TABELAS DE EXECUÇÃO DOS PLANOS POR PROJETOS ###
###################################################

#==============#
#== PROJETOS ==#
#==============#


class Projeto(models.Model):
    # CATEGORIAS_DE_PROJETOS = [
    #     ('Projeto socioambiental', (
    #         ('01', 'Projeto regional'),
    #         ('02', 'Projeto municipal'),
    #     )),
    #     ('Evento acadêmico', ( 
    #         ('03', 'Congresso'),
    #         ('04', 'Seminário'),
    #         ('05', 'Fórum'),
    #         ('06', 'Simpósio'),
    #         ('07', 'Colóquio'),
    #         ('08', 'Painel'),
    #         ('09', 'Reunião acadêmica'),
    #         ('10', 'Outro evento acadêmico'),
    #     )),
    #     ('Evento não-acadêmico', (
    #         ('11', 'Festa ou celebração'),
    #         ('12', 'Feira ou mercado'),
    #         ('13', 'Exibição ou exposição'),
    #         ('14', 'Campanha ou mobilização'),
    #         ('15', 'Curso ou treinamento'),
    #         ('16', 'Outro evento não-acadêmico'),
    #     )),
    #     ('Mini-projetos', (
    #         ('17', 'Projeto de restauração'),
    #         ('18', 'Projeto de remediação'),
    #         ('19', 'Projeto de fauna')
    #         ('20', 'Plano de manejo',),            
    #         ('21', 'Plano de comunicação'),
    #         ('22', 'Plano de monitoramento'),
    #         ('23', 'Outro projeto menor'),
    #     )),
    #     ('Outros projetos', (
    #         ('24', 'Construção ou edificação,'),
    #         ('25', 'Pesquisa ou estudo'),
    #         ('26', 'Outra categoria qualquer'),
    #     )),
    # ]
    
    nome = models.CharField(
        'Nome ou título', 
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
        help_text='Selecione à situação atual do projeto.' 
        choices=BOOL_CHOICES, 
        blank=True, 
        null=False,
        default=True,
        )

    categoria = models.OneToOneField(
        'categorias.Categoria_de_projeto', 
        on_delete=models.SET_NULL, 
        #choices = CATEGORIAS_DE_PROJETOS,
        blank=True, 
        null=True,
        verbose_name='Categoria de projeto', 
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
#== OBJETIVOs ESPECÍFICOS ==#
#===========================#

class Obj_esp(models.Model):    
    nome = models.CharField(
        'Nome ou título', 
        help_text='Defina um título ou nome para o objetivo específico.', 
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

    #BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))

    alcancado = models.BooleanField(
        'Alcançado', 
        #choices=BOOL_CHOICES, 
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

class MetaObj(models.Model):
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
        ))
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
    
    nome = models.CharField(
        'Nome ou título', 
        help_text='Defina um título para a atividade.',  
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

    base_curricular = models.TextField(
        'Base curricular', 
        max_length=300, 
        help_text='Se for atividade docente, descreva brevemente as relações com a base curricular vigente.', 
        blank=True,
        null=True,
        )

    categoria = models.CharField(
        'Categoria', 
        choices = CATEGORIAS_DE_ATIVIDADES, 
        help_text='Selecione uma das categorias de atividades ou tarefas disponíveis', 
        max_length=100,
        blank=True,
        null=True,
        )

    #BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))

    executada = models.BooleanField(
        'Concluída',
        help_text='Marque a caix de seleção se esta atividade já está concluída ou já foi executada', 
        #choices=BOOL_CHOICES, 
        blank=True, 
        null=False,
        default=False,
        )

    coordenador = models.ForeignKey(
        'pessoas.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Selecione a pessoa responsável pela atividade (coordenador, âncora).', 
        blank=True, 
        null=True, 
        verbose_name='Responsável pela atividade', 
        )

    etapa_vinculada = models.ForeignKey(
        Etapa, 
        on_delete=models.SET_NULL, 
        help_text='Insira a etapa que esta atividade está diretamente vinculada, se houver',
        blank=True,
        null=True, 
        verbose_name='Etapa vinculada', 
    )

    meta_vinculada = models.ForeignKey(
        MetaObj, 
        on_delete=models.SET_NULL, 
        help_text='Selecione a meta a que esta atividade se vincula, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Meta vinculada', 
        )

    obj_esp_vinculado = models.ForeignKey(
        Obj_esp, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o objetivo específico a que esta atividade se vincula, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Objetivo específico vinculado', 
        )

    proj_vinculado = models.ForeignKey(
        Projeto, 
        on_delete=models.SET_NULL, 
        help_text='Insira o projeto ao qual essa atividade se vincula',
        blank=True, 
        null=True, 
        verbose_name='Projeto vinculado', 
    )

    local_vinculado = models.ForeignKey(
        'places.Local', 
        on_delete=models.SET_NULL, 
        help_text='Selecione o local de referência onde esta etapa ou atividade está vinculada, se houver',
        blank=True, 
        null=True, 
        verbose_name='Local de referência vinculado',
    )
    
    municipio = models.ForeignKey(
        'places.Municipio',  
        on_delete=models.SET_NULL, 
        verbose_name='Município sede da atividade', 
        blank=True,
        null=True,
        )

    onde = models.CharField(
        'Onde ocorreu a atividade', 
        max_length=120, 
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
    
    final = models.DateTimeField(
        'Fim',
        default=None, 
        help_text='Especifique a data e hora de finalização da atividade.', 
        blank=True,
        null=True,  
        )
    
    resultados = models.TextField(
        'Resultados', 
        max_length=600, 
        help_text='Descreva o que se alcançou com a atividade após concluída.', 
        blank=True,
        null=True,
        )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    arquivos = models.FileField(
        upload_to=r'projects_media\atv_media', 
        blank=True, 
        null=True,
        )

    # def get_absolute_url(self):
    #     """Traz a URL de perfil da Atividade."""
    #     return reverse('atividade-detalhe', args=[str(self.id)])

    def __str__(self):
        return 'ATV' + str(self.id).zfill(5) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Atividade'
        verbose_name_plural = '14 - Atividades'
