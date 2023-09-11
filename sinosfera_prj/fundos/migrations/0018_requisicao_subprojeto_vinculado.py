# Generated by Django 4.2.4 on 2023-09-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundos', '0017_remove_requisicao_objetivo_especifico_vinculado'),
        ('projetos', '0013_subprojeto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisicao',
            name='subprojeto_vinculado',
            field=models.ManyToManyField(blank=True, help_text='Selecione os subprojetos a que esta solicitação está diretamente vinculada.', to='projetos.subprojeto', verbose_name='Subprojeto(s) vinculado(s) à solicitação de fundos'),
        ),
    ]
