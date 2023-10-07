# Generated by Django 4.2.4 on 2023-09-25 11:45

import datetime
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
        ('pessoas', '0001_initial'),
        ('instituicoes', '0002_initial'),
        ('programas', '0001_initial'),
        ('locais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina um título ou nome curto para a atividade36+.', max_length=120, null=True, verbose_name='Nome ou título da atividade')),
                ('descricao', models.TextField(blank=True, help_text='Descreva a atividade com o maior número possível de detalhes relevantes.', null=True, verbose_name='Descrição')),
                ('inicio', models.DateTimeField(blank=True, default=None, help_text='Especifique a data e hora de início da atividade.', null=True, verbose_name='Início')),
                ('fim', models.DateTimeField(blank=True, default=None, help_text='Especifique a data e hora de finalização da atividade.', null=True, verbose_name='Fim')),
                ('concluida', models.BooleanField(blank=True, default=False, help_text='Marque a caixa de seleção se esta atividade já está concluída ou já foi executada.', verbose_name='Concluída')),
                ('base_curricular_vinculada', models.TextField(blank=True, help_text='Se for atividade docente, descreva brevemente as relações com a base curricular vigente.', max_length=300, null=True, verbose_name='Base curricular')),
                ('localizacao', django.contrib.gis.db.models.fields.PointField(blank=True, help_text='Encontre o local da atividade no mapa e depois insira um marcador sobre ele.', null=True, srid=4326, verbose_name='Local da atividade')),
                ('resultados', models.TextField(blank=True, help_text='Registre aqui o que se alcançou com a atividade depois de concluída.', max_length=600, null=True, verbose_name='Resultados')),
                ('publico_envolvido', models.PositiveIntegerField(blank=True, default=0, editable=False, null=True, verbose_name='Público diretamente envolvido')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('arquivos', models.FileField(blank=True, null=True, upload_to='projetos/atividades')),
                ('categoria_de_atividade', models.ForeignKey(blank=True, help_text='Selecione a categoria mais adequada para esta atividade.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.categoria_de_atividade', verbose_name='Categoria')),
                ('coordenador', models.ForeignKey(blank=True, help_text='Especifique a pessoa âncora ou coordenadora desta atividade.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa', verbose_name='Coordenador(a) de Atividade')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina um nome ou título curto ao projeto.', max_length=120, null=True, verbose_name='Nome ou título do projeto')),
                ('objetivo_geral_do_projeto', models.TextField(blank=True, help_text='Descreva o objetivo geral do projeto, ou o impacto que este deseja causar na sociedade e no meio ambiente.', max_length=600, null=True, verbose_name='Objetivo geral do projeto')),
                ('encerrado', models.BooleanField(blank=True, choices=[(True, 'Ativo'), (False, 'Encerrado')], default=True, help_text='Selecione à situação atual deste projeto.', verbose_name='Situação do Projeto')),
                ('resumo_descritivo_do_projeto', models.TextField(blank=True, help_text='Descreva de modo geral o que é, quem está envolvido, onde se dará a execução, quando deverá ocorrer a execução, como e porque o Projeto será executado.', null=True, verbose_name='Resumo descritivo do Projeto')),
                ('fundos_de_execucao_do_projeto', models.TextField(blank=True, help_text='Descreva suscintamente de onde deverão vir ou vieram os recursos para este Projeto.', null=True, verbose_name='Descrição geral das fontes de recursos do Projeto')),
                ('fundos_estimados_do_verde_sinos', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Especifique o total de fundos do VerdeSinos que este Projeto vai acessar ou acessou.', max_digits=10, verbose_name='Total de fundos do VerdeSinos')),
                ('fundos_estimados_de_contra_partida', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Especifique o total de contra-partida que este projeto vai acessar ou acessou.', max_digits=10, verbose_name='Total de fundos de contra-partida')),
                ('valor_total_do_projeto', models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Valor total do Projeto')),
                ('inicio', models.DateField(blank=True, default=datetime.date.today, help_text='Especifique uma data estimada ou definida de início deste Projeto.', verbose_name='Data de início do Projeto')),
                ('fim', models.DateField(blank=True, default=datetime.date.today, help_text='Especifique uma data estimada ou definida para a conclusão deste Projeto.', verbose_name='Data de fim do Projeto')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('arquivos', models.FileField(blank=True, null=True, upload_to='projetos')),
                ('instituicao_ancora_do_projeto', models.ForeignKey(blank=True, help_text='Selecione a Instituição considerada a proponente principal ou a âncora do Projeto', null=True, on_delete=django.db.models.deletion.SET_NULL, to='instituicoes.instituicao', verbose_name='Instituição âncora do Projeto')),
                ('municipio_ancora_do_projeto', models.ForeignKey(blank=True, help_text='Selecione o município cosiderado a sede ou âncora deste projeto.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='locais.municipio', verbose_name='Município sede ou âncora do Projeto')),
                ('pessoa_ancora_do_projeto', models.ForeignKey(blank=True, help_text='Especifique a pessoa âncora, ou coordenadora deste projeto.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa', verbose_name='Coordenador(a) geral de Projeto')),
                ('programa_vinculado_ao_projeto', models.ForeignKey(blank=True, help_text='Selecione o Programa de mobilização social a que este projeto se vincula.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projetos_vinculados_ao_programa', to='programas.programa', verbose_name='Programa de mobilização a que este projeto se vincula')),
                ('urs_vinculadas_ao_projeto', models.ManyToManyField(blank=True, help_text='Selecione uma ou mais URs que estão diretamente relacionadas ao projeto.', related_name='projetos_vinculados_a_ur', to='locais.unidade_de_referencia', verbose_name='UR(s) vinculada(s) ao Projeto')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Subprojeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina um nome ou título curto para este subprojeto.', max_length=120, null=True, verbose_name='Nome ou título do subprojeto')),
                ('descricao_do_subprojeto', models.TextField(blank=True, help_text='Descreva o que este subprojeto pretende alcançar.', max_length=300, null=True, verbose_name='Descrição do subprojeto')),
                ('indicadores', models.TextField(blank=True, help_text='Especifique aqui o(s) indicador(es) que evidenciarão o alcance deste subprojeto.', max_length=300, null=True, verbose_name='Indicadores')),
                ('verificacao', models.TextField(blank=True, help_text='Especifique aqui como serão verificados os indicadores de conclusão deste subprojeto, isto é que instrumentos, metodologia, processos.', max_length=300, null=True, verbose_name='Métodos de verificação')),
                ('percentual_de_conclusao', models.IntegerField(blank=True, default=0, help_text='Insira um valor de 0 a 100 correspondente ao percentual de conclusão deste subprojeto até o momento.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percentual de alcance atingido')),
                ('inicio', models.DateField(blank=True, default=datetime.date.today, help_text='Especifique uma data de início para o Subprojeto.', verbose_name='Data de início do Subprojeto')),
                ('fim', models.DateField(blank=True, default=datetime.date.today, help_text='Defina uma data para a conclusão do Subprojeto.', verbose_name='Data de fim do Subprojeto')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('arquivos', models.FileField(blank=True, null=True, upload_to='projetos/subprojetos')),
                ('categoria_de_subprojeto', models.ForeignKey(blank=True, help_text='Selecione a categoria mais adequada para este subprojeto.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.categoria_de_subprojeto', verbose_name='Categoria')),
                ('coordenador', models.ForeignKey(blank=True, help_text='Especifique a pessoa âncora ou coordenadora deste subprojeto.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa', verbose_name='Coordenador(a) de Subprojeto')),
                ('projeto_vinculado_ao_subprojeto', models.ForeignKey(blank=True, help_text='Selecione o Projeto a que este Subprojeto se vincula.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetos.projeto', verbose_name='Projeto vinculado')),
                ('subprojetos_relacionados', models.ManyToManyField(blank=True, related_name='subprojetos_relacionados_a_subprojetos', to='projetos.subprojeto', verbose_name='Subprojeto relacionado')),
            ],
            options={
                'verbose_name': 'Subprojeto',
                'verbose_name_plural': 'Subprojetos',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Publico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalhamento', models.CharField(blank=True, help_text='Inclua uma breve descrição do público envolvido.', max_length=250, null=True, verbose_name='Detalhamento')),
                ('quantidade', models.PositiveIntegerField(default=0, help_text='Insira a quantidade de pessoas envolvidas da categoria selecionada.', verbose_name='QTD')),
                ('atividade', models.ForeignKey(blank=True, help_text='Selecione a atividade vinculada ao público envolvido.', null=True, on_delete=django.db.models.deletion.CASCADE, to='projetos.atividade', verbose_name='Atividade vinculada.')),
                ('categoria', models.ForeignKey(blank=True, help_text='Selecione o tipo de público envolvido.', null=True, on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria_de_publico', verbose_name='Categoria de público')),
            ],
            options={
                'verbose_name': 'Público envolvido',
                'verbose_name_plural': 'Públicos envolvidos',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina um nome ou título para a etapa de um Subprojeto.', max_length=120, null=True, verbose_name='Nome ou título da etapa')),
                ('descricao', models.TextField(blank=True, help_text='Descreva suscintamente a etapa com algumas atividades que serão necessárias para concluí-la.', max_length=600, null=True, verbose_name='Descrição da etapa')),
                ('concluida', models.BooleanField(blank=True, default=False, help_text='Marque a caixa de seleção se a etapa já está concluída', verbose_name='Concluida')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('coordenador', models.ForeignKey(blank=True, help_text='Selecione a pessoa âncora, coordenadora, responsável pela etapa.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa', verbose_name='Coordenador(a) de etapa')),
                ('subprojeto_vinculado_a_etapa', models.ForeignKey(blank=True, help_text='Selecione o Subprojeto a que esta etapa se vincula.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetos.subprojeto', verbose_name='Subprojeto vinculado à etapa')),
            ],
            options={
                'verbose_name': 'Etapa',
                'verbose_name_plural': 'Etapas',
                'ordering': ('nome',),
            },
        ),
        migrations.AddField(
            model_name='atividade',
            name='etapa_vinculada_a_atividade',
            field=models.ForeignKey(blank=True, help_text='Insira a etapa que esta atividade está diretamente vinculada, se houver', null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetos.etapa', verbose_name='Etapa vinculada'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locais.municipio', verbose_name='Município sede da atividade'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='projeto_vinculado_a_atividade',
            field=models.ForeignKey(blank=True, help_text='Insira o projeto ao qual essa atividade se vincula', null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetos.projeto', verbose_name='Projeto vinculado'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='subcategoria_de_atividade',
            field=models.ForeignKey(blank=True, help_text='Selecione a subcategoria da atividade.', null=True, on_delete=django.db.models.deletion.CASCADE, to='categorias.subcategoria_de_atividade', verbose_name='Subcategoria'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='subprojeto_vinculado_a_atividade',
            field=models.ForeignKey(blank=True, help_text='Selecione o objetivo específico a que esta atividade se vincula, se houver.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetos.subprojeto', verbose_name='Objetivo específico vinculado'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='ur_vinculada',
            field=models.ForeignKey(blank=True, help_text='Selecione o local de referência onde esta atividade está vinculada, se houver', null=True, on_delete=django.db.models.deletion.SET_NULL, to='locais.unidade_de_referencia', verbose_name='Unidade de referência vinculada'),
        ),
    ]