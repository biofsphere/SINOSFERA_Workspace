# Generated by Django 4.2.4 on 2023-09-11 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundos', '0018_requisicao_subprojeto_vinculado'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='id_codificada',
            field=models.CharField(blank=True, editable=False, max_length=60, null=True, unique=True, verbose_name='ID Codificada'),
        ),
        migrations.AddField(
            model_name='requisicao',
            name='id_codificada',
            field=models.CharField(blank=True, editable=False, max_length=60, null=True, unique=True, verbose_name='ID Codificada'),
        ),
    ]
