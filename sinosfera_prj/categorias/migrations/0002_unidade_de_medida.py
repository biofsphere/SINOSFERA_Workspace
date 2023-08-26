# Generated by Django 4.2.4 on 2023-08-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidade_de_medida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina uma profissão ainda não existente no sistema', max_length=30, null=True, unique=True)),
                ('abreviatura', models.CharField(blank=True, help_text='Abreviação da unidade de medida.', max_length=5, null=True, unique=True)),
                ('descricao', models.TextField(blank=True, help_text='Descrição da unidade de medida.', max_length=300, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Unidade de medida',
                'verbose_name_plural': 'Unidades de medida',
                'ordering': ('nome',),
            },
        ),
    ]
