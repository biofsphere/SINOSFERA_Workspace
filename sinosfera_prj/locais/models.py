
from django.db import models

#================#
#== MUNICÍPIOS ==#
#================#

class Municipio(models.Model):
    nome = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        unique=True,
    )

    def __str__(self):
        return 'MUN' + str(self.id).zfill(3) + '-' + self.nome


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'