# Generated by Django 4.2.4 on 2023-09-12 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locais', '0001_initial'),
        ('pessoas', '0001_initial'),
        ('instituicoes', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidade_de_referencia',
            name='proprietario_pf_de_ur',
            field=models.ForeignKey(blank=True, help_text='Selecione o nome do proprietário do local se for Pessoa Física.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa', verbose_name='Pessoa física proprietária do local'),
        ),
        migrations.AddField(
            model_name='unidade_de_referencia',
            name='proprietario_pj_de_ur',
            field=models.ForeignKey(blank=True, help_text='Selecione uma instituição proprietária da UR, se for Pessoa Jurídica.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='instituicoes.instituicao', verbose_name='Pessoa jurídica proprietária do local'),
        ),
    ]
