# Generated by Django 4.2.4 on 2023-09-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_de_atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina uma categoria à atividade ainda não existente no sistema.', max_length=60, null=True, unique=True)),
                ('descricao', models.TextField(blank=True, help_text='Descreva esta categoria no âmbito das atividades.', max_length=300, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria de atividade',
                'verbose_name_plural': 'Categorias de atividade',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Categoria_de_despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina uma categoria de itens de despesa.', max_length=50, null=True, unique=True)),
                ('descricao', models.TextField(blank=True, help_text='Descrição de categoria de itens de despesa.', max_length=300, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoria de despesa',
                'verbose_name_plural': 'Categorias de despesa',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Categoria_de_plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina uma categoria de plano ainda não existent no sistema.', max_length=150, null=True, unique=True, verbose_name='Categoria de Plano')),
                ('descricao', models.TextField(blank=True, help_text='Descreva suscintamente que grupo de planos esta categoria inclui.', max_length=300, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoria de plano',
                'verbose_name_plural': 'Categorias de planos',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Categoria_de_publico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina uma categoria de público atendido ou envolvido em atividades de projetos.', max_length=100, null=True, unique=True)),
                ('descricao', models.TextField(blank=True, help_text='Descreva que tipo de público esta categoria inclui.', max_length=300, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria de público',
                'verbose_name_plural': 'Categorias de público',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Categoria_de_subprojeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina uma categoria ao subprojeto.', max_length=60, null=True, unique=True)),
                ('descricao', models.TextField(blank=True, help_text='Descreva esta categoria no âmbito dos subprojetos de um projeto.', max_length=300, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoria de subprojeto, objetivo específico ou meta',
                'verbose_name_plural': 'Categorias de subprojetos, objetivos específicos ou metas',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Fundo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina um nome ou título curto para o fundo de financiamento', max_length=120, null=True, unique=True)),
                ('descricao', models.TextField(blank=True, help_text='Propósito do fundo.', max_length=300, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Fundo de financiamento',
                'verbose_name_plural': 'Fundos de financiamento',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Profissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina uma profissão ainda não existente no sistema', max_length=60, null=True, unique=True)),
                ('descricao', models.TextField(blank=True, help_text='Descreva essa profissão no âmbito do que fazem os seus profissionais', max_length=300, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Profissão',
                'verbose_name_plural': 'Profissões',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Subcategoria_de_atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina uma subcategoria da categoria de atividade.', max_length=60, null=True, unique=True)),
                ('descricao', models.TextField(blank=True, help_text='Descreva essa subcategoria de atividade.no âmbito das categorias de atividades.', max_length=300, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Subcategoria de atividade',
                'verbose_name_plural': 'Subcategorias de atividade',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Subcategoria_de_subprojeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina uma subcategoria da categoria de Subprojeto, objetivo específico ou meta.', max_length=120, null=True, unique=True)),
                ('descricao', models.TextField(blank=True, help_text='Descreva essa subcategoria no âmbito dos subprojetos de um projeto.', max_length=300, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Subcategoria de subprojeto, objetivo específico ou meta',
                'verbose_name_plural': 'Subcategorias de subprojetos, objetivos específicos ou metas',
                'ordering': ('nome',),
            },
        ),
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
