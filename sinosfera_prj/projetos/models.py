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
    """Tabela de inserção dos dados relativos aos projetos municipais, em sua grande maioria. Outros projetos podem ser inseridos, mas a tabela foi construída com base nas necessidades de projetos municipais vinculados ao VerdeSinos.""",
    programa_vinculado = models.ForeignKey(
        'programas.Programa',
        on_delete=models.SET_NULL,
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
        )
    fundos_estimados_de_contra_partida = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Especifique o total de contra-partida que este projeto vai acessar ou acessou.',
        verbose_name='Total de fundos de contra-partida',
        )
    valor_total_do_projeto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        verbose_name='Valor total do Projeto',
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
    
    def save_model(self, request, obj, form, change):
        """Grava usuário logado que gravou o item"""
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def save(self, *args, **kwargs):
        """Grava o modelo com o valor total do Projeto."""
        self.valor_total_do_projeto = self.fundos_estimados_do_verde_sinos + self.fundos_estimados_de_contra_partida
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Traz a URL de perfil do Projeto."""
        return reverse('projeto-detalhe', args=[str(self.id)])

    def __str__(self):
        return 'PRJ' + str(self.id).zfill(3) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'


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
        Projeto,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Selecione o Projeto a que estes Sub-projeto se vincula.',
        verbose_name='Projeto a que este Sub-projeto se vincula',
        )
    categoria_de_subprojeto = models.CharField(
        max_length=2,
        choices=CATEGORIAS_DE_SUB_PROJETOS
        help_text='Selecione a categoria mais adequada para este Sub-projeto.',
        verbose_name='Categoria de Sub-projeto',
        )
    nome = models.CharField(
        'Nome ou título do Sub-projeto', 
        help_text='Defina o nome ou título para este Sub-projeto.', 
        max_length=120,
        blank=True,
        null=True,
        )
    objetivo_geral_de_projeto = models.TextField(
        'Objetivo geral do Sub-projeto', 
        help_text='Descreva o objetivo geral deste Sub-projeto.', 
        max_length=300,
        blank=True,
        null=True,
        )
    BOOL_CHOICES = ((True, 'Ativo'), (False, 'Encerrado'))
    encerrado = models.BooleanField(
        'Situação do Sub-projeto',
        help_text='Selecione à situação atual do Sub-projeto.', 
        choices=BOOL_CHOICES, 
        blank=True, 
        null=False,
        default=True,
        )
    coordenador = models.ForeignKey(
        'pessoas.Pessoa', 
        on_delete=models.SET_NULL, 
        help_text='Especifique a pessoa coordenadora deste Sub-projeto.', 
        blank=True, 
        null=True, 
        verbose_name='Coordenador de Sub-projeto', 
        )
    inicio = models.DateField(
        'Data de início do Sub-projeto',
        default=date.today, 
        help_text='Especifique uma data de início para o Sub-projeto.', 
        blank=True,
        null=False, 
        )
    fim = models.DateField(
        'Data de fim do Sub-projeto',
        default=date.today, 
        help_text='Defina uma data para a conclusão do Sub-projeto.', 
        blank=True,
        null=False, 
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to='projetos/sub_projetos', 
        blank=True, 
        null=True,
        )

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'SPR' + str(self.id).zfill(3) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Sub-projeto'
        verbose_name_plural = 'Sub-projetos'


#===========================#
#== OBJETIVOS ESPECÍFICOS ==#
#===========================#

class Objetivo_especifico_de_projeto(models.Model):    
    nome = models.CharField(
        'Nome ou título do objetivo específico do Projeto', 
        help_text='Defina um título ou nome curto para o objetivo específico do projeto.', 
        max_length=120,
        blank=True,
        null=True,
        )
    descricao_do_objetivo_especifico = models.TextField(
        'Descrição do objetivo específico do projeto', 
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
    projeto_vinculado = models.ForeignKey(
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
        upload_to='projetos/objetivos_especificos_de_projeto', 
        blank=True, 
        null=True,
        )

    def __str__(self):
        return 'OBJ' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Objetivo específico'
        verbose_name_plural = 'Objetivos específicos'



#===========#
#== METAS ==#
#===========#

class Meta_de_objetivo_especifico_de_projeto(models.Model):
    CATEGORIAS_DE_METAS = [
        ('01', '01 - Ambiental'),
        ('02', '02 - Social'),
        ('03', '03 - Econômica'),
        ('04', '04 - Outra'),
    ]
    categoria_de_meta = models.CharField(
        'Categoria de meta',
        choices = CATEGORIAS_DE_METAS,  
        help_text='Selecione a categoria que essa meta se enquadra melhor.', 
        max_length=100,
        blank=True, 
        null=True, 
    )
    nome = models.CharField(
        'Nome ou título da meta', 
        help_text='Defina um título ou nome curto para a meta que deseja alcançar.', 
        max_length=120,
        blank=True,
        null=True,
        )
    descricao = models.TextField(
        'Descrição da meta', 
        help_text='Descreva a meta detalhadamente, de forma específica, mensurável, alcançável dentro de um prazo hábil.', 
        max_length=600,
        blank=True,
        null=True,
        )
    indicadores = models.TextField(
        'Indicadores', 
        max_length=300, 
        help_text="Considere a categoria da meta e especifique aqui o(s) indicador(es) quantitativo(s) que evidenciarão o seu alcance.", 
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
    prazo = models.DateField(
        'Prazo',
        help_text='Data em que se espera que esta meta seja atingida.',
        blank=True, 
        null=True, 
    )
    alcancada = models.BooleanField(
        'Alcançada', 
        blank=True, 
        null=False,
        default=False,
        help_text='Marque a caxa de seleção se essa meta já foi alcançada.',
        )
    objetivo_especifico_vinculado_a_meta = models.ForeignKey(
        Objetivo_especifico_de_projeto, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o objetivo específico de Projeto a que esta Meta se vincula.', 
        blank=True, 
        null=True, 
        verbose_name='Objetivo específico vinculado à Meta', 
        )
    projeto_vinculado_a_meta = models.ForeignKey(
        Projeto, 
        on_delete=models.SET_NULL, 
        help_text='Selecione o Projeto a que esta Meta está vinculada.',
        blank=True, 
        null=True, 
        verbose_name='Projeto vinculado a Meta', 
    )
    coordenador_de_meta = models.ForeignKey(
        'people.Pessoa',  
        on_delete=models.SET_NULL, 
        help_text='Selecione a pessoa âncora ou coordenadora desta meta, se houver.', 
        blank=True, 
        null=True, 
        verbose_name='Coordenador geral de Meta', 
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivos = models.FileField(
        upload_to='projetos\metas', 
        blank=True, 
        null=True,
        )

    def __str__(self):
        return 'MET' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Meta'
        verbose_name_plural = 'Metas'



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
