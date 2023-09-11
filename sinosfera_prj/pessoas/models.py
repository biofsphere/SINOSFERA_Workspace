
from django.db import models
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

custom_username_validators = [ASCIIUsernameValidator()]

# ============================= #
# == PESSOAS E COORDENADORES == #
# ============================= #

class CustomUser(AbstractUser):
    """
        Generates a user model to enalbe customizations.
    """
    def get_item_id(self):
        return 'USU' + str(self.id).zfill(3) + '-' + str(self.username)
    get_item_id.short_description = 'ID Codificada'  # Set the custom column header name

    def __str__(self):
        return 'USU' + str(self.id).zfill(3) + '-' + str(self.username)


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'



class Pessoa(models.Model):
    """
        Extends User data with several fields.
    """    
    nome_completo = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        )
    conta_associada = models.OneToOneField(
        CustomUser, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        verbose_name='Conta associada à pessoa',
        help_text='Selecione a conta associada à pessoa se houver',
        )
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    telefone_celular = models.CharField(
        'Telefone celular',
        validators = [phoneNumberRegex], 
        max_length = 16, 
        help_text='Insira somente dígitos e inclua o código de área do seu telefone celular.',
        blank=True,
        null=True,
        unique=True,
        )
    email = models.EmailField(
        'E-mail', 
        blank=True,
        null=True,
        unique=True,
        )
    profissao = models.ForeignKey(
        'categorias.Profissao',
        on_delete=models.SET_NULL,
        help_text='Selecione a profissão da pessoa no cadastro',
        blank=True,
        null=True,
    )
    municipio_de_trabalho_da_pessoa = models.ForeignKey(
        'locais.Municipio', 
        on_delete=models.SET_NULL,  
        verbose_name='Município', 
        blank=True,
        null=True,
        )
    # ==== Utility fields ==== #
    criado_por = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='perfis_criados', editable=False,)
    criado_em = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    atualizado_por = models.ForeignKey('pessoas.CustomUser', on_delete=models.SET_NULL, blank=True, null=True, related_name='perfis_atualizados', editable=False,)
    atualizado_em = models.DateTimeField(auto_now=True, blank=True, null=True,)
    id_codificada = models.CharField(
        max_length=60, 
        blank=True,
        null=True,
        verbose_name='ID Codificada',
        editable=False,
        unique=True,
        )
    
    def save(self, *args, **kwargs):
        self.id_codificada = 'PES' + str(self.id).zfill(3) + '-' + str(self.nome_completo)
        super().save(*args, **kwargs)

    # Signal to populate id_codificada when the object is created
    @receiver(post_save, sender='pessoas.Pessoa')
    def populate_id_codificada(sender, instance, created, **kwargs):
        if created:
            # The object is being created, so set id_codificada accordingly
            instance.id_codificada = 'PES' + str(instance.id).zfill(3) + '-' + str(instance.nome_completo)
            instance.save()  # Save the object again to persist the change

    def __str__(self): 
        return str(self.id_codificada)


    class Meta:
        ordering = ('nome_completo',)
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

