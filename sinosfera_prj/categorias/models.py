from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# ##############################
# ### TABELAS DE TIPOLOGIAS  ###
# ##############################


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
    # ==== Utility fields ==== #
    criado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='profissoes_criadas', 
        editable=False,
        )
    criado_em = models.DateTimeField(
        auto_now_add=True, 
        blank=True, 
        null=True,
        )
    atualizado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='profissoes_atualizadas', 
        editable=False,
        )
    atualizado_em = models.DateTimeField(
        auto_now=True, 
        blank=True, 
        null=True,
        )
    # id_codificada = models.CharField(
    #     max_length=60, 
    #     blank=True,
    #     null=True,
    #     verbose_name='ID Codificada',
    #     editable=False,
    #     unique=True,
    #     ) 

    # def save(self, *args, **kwargs):
    #     self.id_codificada = 'PRF' + str(self.id).zfill(3) + '-' + str(self.nome)
    #     super().save(*args, **kwargs)

    # # Signal to populate id_codificada when the object is created
    # @receiver(post_save, sender='categorias.Profissao')
    # def populate_id_codificada(sender, instance, created, **kwargs):
    #     if created:
    #         # The object is being created, so set id_codificada accordingly
    #         instance.id_codificada = 'PRF' + str(instance.id).zfill(3) + '-' + str(instance.nome)
    #         instance.save()  # Save the object again to persist the change

    def __str__(self):
        return str(self.nome)
    

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Profissão'
        verbose_name_plural = 'Profissões'


# #==========================#
# #== CATEGORIAS DE PLANOS ==#
# #==========================#

class Categoria_de_plano(models.Model):
    """Tabela de categorias pré-existentes de planos geralmente plurianuais, os quais podem ser municipais, regionais, ou quaisquer outros escopos geográficos e temporais."""
    nome = models.CharField(
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
    # ==== Utility fields ==== #
    criado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='categorias_de_planos_criadas', 
        editable=False,
        )
    criado_em = models.DateTimeField(
        auto_now_add=True, 
        blank=True, 
        null=True,
        )
    atualizado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='categorias_de_planos_atualizadas', 
        editable=False,
        )
    atualizado_em = models.DateTimeField(
        auto_now=True, 
        blank=True, 
        null=True,
        )

    def __str__(self):
        return str(self.nome)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de plano'
        verbose_name_plural = 'Categorias de planos'

#================================================================================#
#== CATEGORIAS E SUBCATEGORIAS DE SUBPROJETOS  / OBJETIVOS ESPECÍFICOS / METAS ==#
#================================================================================#

class Subcategoria_de_subprojeto(models.Model):
    categoria = models.ForeignKey(
        'Categoria_de_subprojeto',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text='Selecione a categoria de subprojeto, objetivo específico ou meta a que esta subcategoria pertence.',
        verbose_name='Categoria de subprojeto, objetivo específico ou meta',
    )
    nome = models.CharField(
        max_length=120, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma subcategoria da categoria de Subprojeto, objetivo específico ou meta.',
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva essa subcategoria no âmbito dos subprojetos de um projeto.',
    )
    # ==== Utility fields ==== #
    criado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='subcategorias_de_subprojetos', 
        editable=False,
        )
    criado_em = models.DateTimeField(
        auto_now_add=True, 
        blank=True, 
        null=True,
        )
    atualizado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='subcategorias_de_subprojetos_atualizadas', 
        editable=False,
        )
    atualizado_em = models.DateTimeField(
        auto_now=True, 
        blank=True, 
        null=True,
        )

    def __str__(self):
        return str(self.nome)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Subcategoria de subprojeto, objetivo específico ou meta'
        verbose_name_plural = 'Subcategorias de subprojetos, objetivos específicos ou metas'


class Categoria_de_subprojeto(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria ao subprojeto.',
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva esta categoria no âmbito dos subprojetos de um projeto.',
    )
    # ==== Utility fields ==== #
    criado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='categorias_de_subprojetos_criadas', 
        editable=False,
        )
    criado_em = models.DateTimeField(
        auto_now_add=True, 
        blank=True, 
        null=True,
        )
    atualizado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='categorias_de_subprojetos_atualizadas', 
        editable=False,
        )
    atualizado_em = models.DateTimeField(
        auto_now=True, 
        blank=True, 
        null=True,
        )

    def __str__(self):
        return str(self.nome)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de subprojeto, objetivo específico ou meta'
        verbose_name_plural = 'Categorias de subprojetos, objetivos específicos ou metas'


#==============================#
#== CATEGORIAS DE ATIVIDADES ==#
#==============================#

class Subcategoria_de_atividade(models.Model):
    categoria = models.ForeignKey(
        'Categoria_de_atividade',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text='Selecione a categoria de atividade a que esta subcategoria pertence.',
        verbose_name='Categoria de atividade',
    )
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma subcategoria da categoria de atividade.',
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva essa subcategoria de atividade.no âmbito das categorias de atividades.',
    )
    # ==== Utility fields ==== #
    criado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='subcategorias_de_atividade_criadas')
    atualizado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='subcategorias_de_atividades_atualizadas')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nome)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Subcategoria de atividade'
        verbose_name_plural = 'Subcategorias de atividade'


class Categoria_de_atividade(models.Model):
    nome = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria à atividade ainda não existente no sistema.',
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva esta categoria no âmbito das atividades.',
    )
    # ==== Utility fields ==== #
    criado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='categorias_de_atividade_criadas')
    atualizado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='categorias_de_atividades_atualizadas')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nome)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de atividade'
        verbose_name_plural = 'Categorias de atividade'


#======================================#
#== CATEGORIAS DE PÚBLICOS ATENDIDOS ==#
#======================================#

class Categoria_de_publico(models.Model):
    """Tabela de inserção de categorias de públicos envolvidos."""
    nome = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria de público atendido ou envolvido em atividades de projetos.'
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descreva que tipo de público esta categoria inclui.'
    )
    # ==== Utility fields ==== #
    criado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='categorias_de_publico_alvo_criadas')
    atualizado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='categorias_de_publico_alvo_atualizadas')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


    # def save_model(self, request, obj, form, change):
    #     '''Grava usuário logado que gravou o item'''
    #     obj.inserido_por = request.user
    #     super().save_model(request, obj, form, change)

    def __str__(self):
        return str(self.nome)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de público'
        verbose_name_plural = 'Categorias de público'


#=============================================#
#== TIPOS DE ITENS DE DESPESA EM ORÇAMENTOS ==#
#=============================================#

class Categoria_de_despesa(models.Model):
    """Tabela de inserção de categorias de despesa em orçamentos."""
    nome = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma categoria de itens de despesa.'
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descrição de categoria de itens de despesa.'
    )
        # ==== Utility fields ==== #
    criado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='categogiras_de_despesa_criadas', 
        editable=False,
        )
    criado_em = models.DateTimeField(
        auto_now_add=True, 
        blank=True, 
        null=True,
        )
    atualizado_por = models.ForeignKey(
        'pessoas.CustomUser', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='categorias_de_despesas_atualizadas', 
        editable=False,
        )
    atualizado_em = models.DateTimeField(
        auto_now=True, 
        blank=True, 
        null=True,)
    # id_codificada = models.CharField(
    #     max_length=60, 
    #     blank=True,
    #     null=True,
    #     verbose_name='ID Codificada',
    #     editable=False,
    #     unique=True,
    #     )

    def __str__(self):
        return str(self.nome)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Categoria de despesa'
        verbose_name_plural = 'Categorias de despesa'

#==============================================#
#== UNIDADES DE MEDIDA DE ITENS DE ORÇAMENTO ==#
#==============================================#

class Unidade_de_medida(models.Model):
    """Tabela de inserção de Unidades de Medida para elaboração de orçamentos."""
    nome = models.CharField(
        max_length=30, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina uma profissão ainda não existente no sistema'
    )
    abreviatura = models.CharField(
        max_length=5,
        blank=True,
        null=True,
        unique=True,
        help_text='Abreviação da unidade de medida.',
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Descrição da unidade de medida.'
    )
    # ==== Utility fields ==== #
    criado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='unidades_de_medida_criadas')
    atualizado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='unidades_de_medida_atualizadas')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.abreviatura)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Unidade de medida'
        verbose_name_plural = 'Unidades de medida'


#=============================#
#== FUNDOS DE FINANCIAMENTO ==#
#=============================#

class Fundo(models.Model):
    """Tabela de inserção de dados dos fundos de financiamento disponíveis."""
    nome = models.CharField(
        max_length=120, 
        blank=True, 
        null=True, 
        unique=True, 
        help_text='Defina um nome ou título curto para o fundo de financiamento',
    )
    mantenedora = models.ForeignKey(
        'instituicoes.Instituicao',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Instituição mantenedora',
    )
    descricao = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text='Propósito do fundo.'
    )
    criado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='fundos_criados')
    atualizado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='fundos_atualizados')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nome)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Fundo de financiamento'
        verbose_name_plural = 'Fundos de financiamento'