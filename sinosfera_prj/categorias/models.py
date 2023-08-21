from django.db import models

##############################
### TABELAS DE TIPOLOGIAS  ###
##############################

#================================#
#== CATEGORIAS DE INSTITUIÇÕES ==#
#================================#

class Categoria_de_instituicao(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria de instituição ainda não existente no sistema'
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva esta categoria no âmbito das instituições'
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'CIN' + str(self.id).zfill(2) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de instituição'
        verbose_name_plural = 'Categorias de instituições'

#==========================================#
#== CATEGORIAS DE UNIDADES DE REFERÊNCIA ==#
#==========================================#

class Categoria_de_ur(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria de unidade de referência ainda não existente no sistema'
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva esta categoria no âmbito dos locais de referência'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'CUR' + str(self.id).zfill(2) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de unidade de referência'
        verbose_name_plural = 'Categorias de unidades de referência'


#========================================#
#== CATEGORIAS DE PESSOAS (PROFISSÕES) ==#
#========================================#

class Profissao(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma profissão ainda não existente no sistema'
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva essa profissão no âmbito do que fazem os seus profissionais'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'PRO' + str(self.id).zfill(2) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Profissão'
        verbose_name_plural = 'Profissões'


#=====================================#
#== CATEGORIAS DE PLANOS MUNICIPAIS ==#
#=====================================#

class Categoria_de_plano_plurianual(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria de plano plurianual ainda não existente no sistema'
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva essa categoria no âmbito dos planos plurianuais'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'CPL' + str(self.id).zfill(2) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de plano plurianual'
        verbose_name_plural = 'Categorias de planos plurianuais'


#============================#
#== CATEGORIAS DE PROJETOS ==#
#============================#

class Categoria_de_projeto(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria de projeto ainda não existente no sistema'
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva esta categoria no âmbito dos projetos'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'CPJ' + str(self.id).zfill(2) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de projeto'
        verbose_name_plural = 'Categorias de projetos'


#=========================#
#== CATEGORIAS DE METAS ==#
#=========================#

class Categoria_de_meta(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria de meta ainda não existente no sistema'
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva essa categoria no âmbito das metas'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'CMT' + str(self.id).zfill(2) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de meta'
        verbose_name_plural = 'Categorias de metas'


#==========================#
#== CATEGORIAS DE ETAPAS ==#
#==========================#

class Categoria_de_etapa(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria de etapa ainda não existente no sistema'
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva essa categoria no âmbito das etapas de objetivos específicos ou metas'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'CET' + str(self.id).zfill(2) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de etapa'
        verbose_name_plural = 'Categorias de etapas'


#==============================#
#== CATEGORIAS DE ATIVIDADES ==#
#==============================#

class Categoria_de_atividade(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria de atividade ainda não existente no sistema'
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva essa categoria no âmbito das atividades'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'CAT' + str(self.id).zfill(2) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de atividade'
        verbose_name_plural = 'Categorias de atividades'
