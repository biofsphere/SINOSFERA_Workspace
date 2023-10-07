# Generated by Django 4.2.4 on 2023-09-25 11:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(blank=True, default='', help_text='Insira a razão social da instituição como consta no CNPJ ou o nome completo da mesma', max_length=150, null=True, verbose_name='Razão Social')),
                ('nome_fantasia', models.CharField(blank=True, default='', help_text='Insira a sigla ou nome fantasia da instituição como consta no CNPJ ou o nome como é conhecida', max_length=60, null=True, verbose_name='Nome fantasia')),
                ('sem_cnpj', models.BooleanField(blank=True, default=False, help_text='Marque a caixa de seleção se a Instituição não possui CNPJ.', verbose_name='Instituição sem CNPJ')),
                ('cnpj', models.CharField(blank=True, help_text='Insira somente os 14 dígitos do CNPJ.', max_length=18, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{14}$')], verbose_name='CNPJ')),
                ('telefone', models.CharField(blank=True, help_text='Insira somente dígitos e Inclua o código de área', max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Telefone comercial')),
                ('email', models.EmailField(blank=True, default=' ', max_length=254, null=True, verbose_name='E-mail')),
                ('url', models.URLField(blank=True, default='', null=True, verbose_name='URL')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('arquivos', models.FileField(blank=True, null=True, upload_to='locais/instituicoes')),
            ],
            options={
                'verbose_name': 'Instituição',
                'verbose_name_plural': 'Instituições',
                'ordering': ('nome_fantasia',),
            },
        ),
    ]