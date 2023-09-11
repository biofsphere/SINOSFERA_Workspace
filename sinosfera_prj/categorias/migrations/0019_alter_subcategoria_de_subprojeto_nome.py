# Generated by Django 4.2.4 on 2023-09-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0018_remove_categoria_de_atividade_subcategorias_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoria_de_subprojeto',
            name='nome',
            field=models.CharField(blank=True, help_text='Defina uma subcategoria da categoria de Subprojeto, objetivo específico ou meta.', max_length=120, null=True, unique=True),
        ),
    ]
