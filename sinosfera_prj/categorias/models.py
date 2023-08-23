from django.db import models


# ##############################
# ### TABELAS DE TIPOLOGIAS  ###
# ##############################

# #================================#
# #== CATEGORIAS DE INSTITUIÇÕES ==#
# #================================#

# class Categoria_de_instituicao(models.Model):
#     nome = models.CharField(
#         max_length=60, 
#         blank=True, 
#         null=True, 
#         unique=True, 
#         help_text='Defina uma categoria de instituição ainda não existente no sistema'
#     )
#     descricao = models.TextField(
#         max_length=300,
#         blank=True,
#         null=True,
#         help_text='Descreva esta categoria no âmbito das instituições'
#     )

#     criado_em = models.DateTimeField(auto_now_add=True)
#     atualizado_em = models.DateTimeField(auto_now=True)


#     def save_model(self, request, obj, form, change):
#         '''Grava usuário logado que gravou o item'''
#         obj.inserido_por = request.user
#         super().save_model(request, obj, form, change)

#     def __str__(self):
#         return 'CIN' + str(self.id).zfill(2) + '-' + self.nome

#     class Meta:
#         ordering = ('nome',)
#         verbose_name = 'Categoria de instituição'
#         verbose_name_plural = 'Categorias de instituições'

# #==========================================#
# #== CATEGORIAS DE UNIDADES DE REFERÊNCIA ==#
# #==========================================#

# class Categoria_de_ur(models.Model):
#     nome = models.CharField(
#         max_length=60, 
#         blank=True, 
#         null=True, 
#         unique=True, 
#         help_text='Defina uma categoria de unidade de referência ainda não existente no sistema'
#     )
#     descricao = models.TextField(
#         max_length=300,
#         blank=True,
#         null=True,
#         help_text='Descreva esta categoria no âmbito dos locais de referência'
#     )
#     criado_em = models.DateTimeField(auto_now_add=True)
#     atualizado_em = models.DateTimeField(auto_now=True)

#     def save_model(self, request, obj, form, change):
#         '''Grava usuário logado que gravou o item'''
#         obj.inserido_por = request.user
#         super().save_model(request, obj, form, change)

#     def __str__(self):
#         return 'CUR' + str(self.id).zfill(2) + '-' + self.nome

#     class Meta:
#         ordering = ('nome',)
#         verbose_name = 'Categoria de unidade de referência'
#         verbose_name_plural = 'Categorias de unidades de referência'

#========================================#
#== CATEGORIAS DE PESSOAS (PROFISSÕES) ==#
#========================================#

class Profissao(models.Model):
    """Tabela de inserção de Profissões como atributo as Pessoas que serão registradas no sistema."""
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
        return 'PRO' + str(self.id).zfill(3) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Profissão'
        verbose_name_plural = 'Profissões'


# #==========================#
# #== CATEGORIAS DE PLANOS ==#
# #==========================#

class Categoria_de_plano(models.Model):
    """Tabela de categorias pré-existentes de planos geralmente plurianuais, os quais podem ser municipais, regionais, ou quaisquer outros escopos geográficos e temporais."""
    nome_da_categoria_de_plano = models.CharField(
        'Categoria de Plano',
        max_length=150,
        help_text='Defina uma categoria de plano ainda não existent no sistema.',
        blank=True,
        null=True,
        unique=True,
        )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva suscintamente que grupo de planos esta categoria inclui.',
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'CPL' + str(self.id).zfill(2) + '-' + self.nome_da_categoria_de_plano

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de plano'
        verbose_name_plural = 'Categorias'


#================================================================#
#== CATEGORIAS DE OBJETIVOS ESPECÍFICOS / SUB-PROJETOS / METAS ==#
#================================================================#

#====================================================================#
#== SUB-CATEGORIAS DE OBJETIVOS ESPECÍFICOS / SUB-PROJETOS / METAS ==#
#====================================================================#

class Sub_categoria_de_objetivo_especifico(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma sub-categoria da categoria de objetivo específico, sub-projeto ou meta.',
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva essa sub-categoria no âmbito dos objetivos específicos de um projeto.',
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'SCO' + str(self.id).zfill(2) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Sub-categoria de objetivo específico'
        verbose_name_plural = 'Sub-categorias de objetivos específicos'


class Categoria_de_objetivo_especifico(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria ao Objetivo Especifico ainda não existente no sistema.',
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva esta categoria no âmbito dos objetivos específicos de um projeto.',
    )
    sub_categorias = models.ManyToManyField(
        'Sub_categoria_de_objetivo_especifico', 
        related_name='Categorias_de_objetivos_especificos',
        
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        '''Grava usuário logado que gravou o item'''
        obj.inserido_por = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return 'COB' + str(self.id).zfill(2) + '-' + self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de objetivo, sub-projeto ou meta'
        verbose_name_plural = 'Categorias de objetivos, sub-projetos ou metas'





# #==========================#
# #== CATEGORIAS DE ETAPAS ==#
# #==========================#

# class Categoria_de_etapa(models.Model):
#     nome = models.CharField(
#         max_length=60, 
#         blank=True, 
#         null=True, 
#         unique=True, 
#         help_text='Defina uma categoria de etapa ainda não existente no sistema'
#     )
#     descricao = models.TextField(
#         max_length=300,
#         blank=True,
#         null=True,
#         help_text='Descreva essa categoria no âmbito das etapas de objetivos específicos ou metas'
#     )
#     criado_em = models.DateTimeField(auto_now_add=True)
#     atualizado_em = models.DateTimeField(auto_now=True)

#     def save_model(self, request, obj, form, change):
#         '''Grava usuário logado que gravou o item'''
#         obj.inserido_por = request.user
#         super().save_model(request, obj, form, change)

#     def __str__(self):
#         return 'CET' + str(self.id).zfill(2) + '-' + self.nome

#     class Meta:
#         ordering = ('nome',)
#         verbose_name = 'Categoria de etapa'
#         verbose_name_plural = 'Categorias de etapas'


# #==============================#
# #== CATEGORIAS DE ATIVIDADES ==#
# #==============================#

# class Categoria_de_atividade(models.Model):
#     nome = models.CharField(
#         max_length=60, 
#         blank=True, 
#         null=True, 
#         unique=True, 
#         help_text='Defina uma categoria de atividade ainda não existente no sistema'
#     )
#     descricao = models.TextField(
#         max_length=300,
#         blank=True,
#         null=True,
#         help_text='Descreva essa categoria no âmbito das atividades'
#     )
#     criado_em = models.DateTimeField(auto_now_add=True)
#     atualizado_em = models.DateTimeField(auto_now=True)

#     def save_model(self, request, obj, form, change):
#         '''Grava usuário logado que gravou o item'''
#         obj.inserido_por = request.user
#         super().save_model(request, obj, form, change)

#     def __str__(self):
#         return 'CAT' + str(self.id).zfill(2) + '-' + self.nome

#     class Meta:
#         ordering = ('nome',)
#         verbose_name = 'Categoria de atividade'
#         verbose_name_plural = 'Categorias de atividades'
