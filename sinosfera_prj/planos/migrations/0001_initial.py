# Generated by Django 4.2.4 on 2023-08-25 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locais', '0002_microbacia_alter_municipio_nome_and_more'),
        ('pessoas', '0002_rename_user_pessoa_usuario_pessoa_profissao'),
        ('categorias', '0001_initial'),
        ('instituicoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina um nome curto para o Plano.', max_length=150, null=True, verbose_name='Nome ou título do Plano')),
                ('objetivo_geral_do_plano', models.TextField(blank=True, help_text='Descreva de modo geral o que o Plano pretende alcançar na sociedade e no meio ambiente.', null=True, verbose_name='Objetivo geral do Plano')),
                ('resumo_descritivo_do_plano', models.TextField(blank=True, help_text='Descreva de modo geral o que é, quem está envolvido, onde se dará a execução, quando deverá ocorrer a execução, como e porque o Plano será executado.', null=True, verbose_name='Resumo descritivo do Plano')),
                ('fundos_de_execucao_do_plano', models.TextField(blank=True, help_text='Descreva brevemente as fontes de recursos para execução deste Plano.', null=True, verbose_name='Fundos de execução do Plano')),
                ('prazo_de_execucao_do_plano', models.CharField(blank=True, choices=[('ML', 'MUITO LONGO (mais de 8 anos)'), ('L', 'LONGO (de 4 a 8 anos)'), ('M', 'MÉDIO (de dois a 4 anos)'), ('C', 'CURTO (de 1 a dois anos)'), ('MC', 'MUITO CURTO (menos de 1 ano)')], help_text='Selecione o prazo estabelecido para execução completa deste Plano', max_length=2, null=True)),
                ('escopo_geografico_do_plano', models.CharField(blank=True, choices=[('NAC', 'Nacional'), ('MRE', 'Macroregional'), ('EST', 'Estadual'), ('MIC', 'Microregional'), ('MUN', 'Municipal'), ('LOC', 'Local')], help_text='Selecione o escopo geográfico do Plano', max_length=3, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('arquivos', models.FileField(blank=True, null=True, upload_to='planos')),
                ('categoria', models.ForeignKey(blank=True, help_text='Selecione uma categoria para este plano. Se não existir, insira uma categoria nova clicando em "+".', null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.categoria_de_plano')),
                ('instituicao_ancora_do_plano', models.ForeignKey(blank=True, help_text='Selecione a Instituição considerada a proponente principal ou a âncora do Plano', null=True, on_delete=django.db.models.deletion.SET_NULL, to='instituicoes.instituicao', verbose_name='Instituição âncora do Plano')),
                ('municipio_ancora_do_plano', models.ForeignKey(blank=True, help_text='Selecione o município cosiderado a sede ou âncora deste plano.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='locais.municipio', verbose_name='Município âncora do Plano')),
                ('pessoa_ancora_do_plano', models.ForeignKey(blank=True, help_text='Especifique a pessoa âncora, ou coordenadora deste plano, se houver.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa', verbose_name='Coordenador geral')),
            ],
            options={
                'verbose_name': 'Plano',
                'verbose_name_plural': '07 - Planos',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Programa_de_acoes_prioritarias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina um nome ou título curto para o program de ações prioritárias do plano.', max_length=120, null=True, verbose_name='Nome ou título do programa de ações prioritárias')),
                ('objetivo_geral_do_programa_de_acoes_prioritarias', models.TextField(blank=True, help_text='Descreva de modo geral o que o programa de ações deseja alcançar.', max_length=600, null=True, verbose_name='Objetivo geral do programa de ações prioritárias')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('coordenador', models.ForeignKey(blank=True, help_text='Selecione uma pessoa âncora ou coordenadora do programa de ações prioritárias.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa', verbose_name='Coordenador geral do programa de ações prioritárias')),
                ('plano_vinculado_ao_programa_de_acoes_prioritarias', models.ForeignKey(blank=True, help_text='Especifique a qual plano plurianual este programa de ações prioritárias está vinculado.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='planos.plano', verbose_name='Plano vinculado')),
            ],
            options={
                'verbose_name': 'Programa de ações prioritárias',
                'verbose_name_plural': '08 - Programas de ações prioritárias',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Acao_prioritaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Defina um nome ou título curto para a ação prioritária.', max_length=120, null=True, verbose_name='Nome ou título da ação prioritária')),
                ('objetivo_geral', models.TextField(blank=True, help_text='Descreva de modo geral o que esta ação prioritária deseja alcançar.', max_length=600, null=True, verbose_name='Objetivo geral da ação prioritária')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('coordenador', models.ForeignKey(blank=True, help_text='Selecione a pessoa âncora ou coordenadora desta ação prioritária, se houver.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa', verbose_name='Coordenador geral da ação prioritária')),
                ('programa_de_acoes_prioritarias_vinculado', models.ForeignKey(blank=True, help_text='Selecione o programa de ações prioritárias a esta ação está vinculada.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='planos.programa_de_acoes_prioritarias', verbose_name='Programa de ações vinculado')),
            ],
            options={
                'verbose_name': 'Ação prioritária',
                'verbose_name_plural': '09 - Ações prioritárias',
                'ordering': ('nome',),
            },
        ),
    ]
